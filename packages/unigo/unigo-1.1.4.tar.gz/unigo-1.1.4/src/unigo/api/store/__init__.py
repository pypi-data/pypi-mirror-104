from flask import Flask, jsonify, abort, request, make_response, Response
from ..data_objects import CulledGoParametersSchema as goParameterValidator
from ..data_objects import loadUnivGO
from .cache import setCacheType, delTreeByTaxids, storeTreeByTaxid, getTaxidKeys, getUniversalTree
from .cache import getCulledVector, storeCulledVector, getUniversalVector
from .cache import clear as clearStore
from .cache import buildUniversalVector, listTrees, listVectors, listMissUniversalVector, listCulled
from .cache import status as storeStatus
from decorator import decorator
# IF OFFLOADABLE BLOCKING ROUTES KEEP ON SHOWING UP
# https://blog.miguelgrinberg.com/post/using-celery-with-flask

import time

from multiprocessing import Process, Value, Semaphore

bSemaphore = None
C_TYPE = None
_MAIN_ = False

def bootstrap(newElem=None, cacheType='local',\
    clear=False, _main_=False, **kwargs):
    global _MAIN_, C_TYPE
    
    if _main_:
        print("Bootstraping main process")
        _MAIN_ = _main_
        global bSemaphore
        bSemaphore = Semaphore(1) # bleeding eyes
        setCacheType(cacheType, **kwargs)
        C_TYPE = cacheType
        if clear:
            clearStore()

        if newElem:
            print("Boostraping unigo store with following new ressources")
            for taxid, tree in newElem:
                print(f"\tAdding{taxid}:{tree}")
                storeTreeByTaxid(tree, taxid)

        tcount, vcount, _vcount = storeStatus()
        print(f"Database content:\n\t{tcount} trees, {vcount} vectors, {_vcount} culled")

        app = Flask(__name__)

        app.add_url_rule('/ping', 'ping', ping)
        
        app.add_url_rule('/taxids', 'view_taxids', view_taxids)
        
        app.add_url_rule('/unigo/<taxid>', 'view_unigo', view_unigo, methods=['GET'])
        
        app.add_url_rule('/vector/<taxid>', 'view_vector', view_vector, methods=['GET'])
        
        app.add_url_rule("/vector/<taxid>", 'view_culled_vector', view_culled_vector, methods=['POST'])
        
        app.add_url_rule('/add/unigo/<taxid>', 'add_unigo', add_unigo, methods=['POST'])

        app.add_url_rule('/del/unigo/<taxid>', 'del_unigo', del_unigo, methods=['DELETE'])

        app.add_url_rule('/build/vectors', 'build_vectors', build_vectors)

        app.add_url_rule('/list/<elemType>', 'list_elements', list_elements)

        return app

def list_elements(elemType):
    if elemType == 'vectors':
        return jsonify({ 'vectors': listVectors() })
      
    elif elemType == 'trees':
        return jsonify({ 'trees': listTrees() })
    
    elif elemType == 'culled':
        return jsonify({ 'culled': listCulled() })


    print(f"Unknwon element type {elemType} to list")
    abort(404)

# CPU intensive route -> offloading it to multiprocess
# using semaphore to prevent concurrency popup on multiple requests
def build_vectors():
    if _MAIN_:
        missUniversalVector = listMissUniversalVector()
        if not missUniversalVector:
            return jsonify({"status": "nothing to build"}), 200

        # global bSemaphore exists
        if bSemaphore.acquire(block=False):
            print(f"bSemaphore is acquired")
            p = Process(
                target=_buildUniversalVector,
                args=(bSemaphore, C_TYPE),
                daemon=True
            )
            p.start()
            return jsonify({
                "status": "starting",
                "targets" : missUniversalVector
            }), 200
        
        print(f"bSemaphore is locked")   
        return jsonify({"status": "running"}), 202
    else: 
        print("##### Twilight zone ######") 


@decorator
def semHolder(fn, _bSemaphore, cacheType, *args, **kwargs):
    #print("Decrorator start")
    setCacheType(cacheType)
    #time.sleep(10)
    fn(*args, **kwargs)
    _bSemaphore.release()
    print(f"Relasing bSemaphore")

@semHolder
def _buildUniversalVector(*args,**kwargs):
    buildUniversalVector()

def ping():
    return "pong"

def view_taxids():
    return str( getTaxidKeys() )

def view_unigo(taxid):
    try:
        tree = getUniversalTree(taxid)
        return jsonify(tree.serialize())
    except KeyError as e:
        print(e)
        abort(404)

##################################################
# ACCESSORS to taxid specific goterms as vectors
##################################################
# GET route, return universal vector
def view_vector(taxid):
    try:
        taxidVector = getUniversalVector(taxid)
    except KeyError as e:
        print(e)
        abort(404)
    
    return jsonify(taxidVector)
# POST route
# Presuming live culling is not CPU intensive enough to
# promote multiprocess offloading:: CHECK IT
def view_culled_vector(taxid): 
    try:
        taxidVector = getUniversalVector(taxid)
    except KeyError as e:
        print(e)
        abort(404)
    try:
        data = request.get_json()
        _goParameterValidator = goParameterValidator()
        goParameter = _goParameterValidator.load(request)
        cmin, cmax, fmax = ( goParameter['minCount'],\
            goParameter['maxCount'], goParameter['maxFreq'])
    except Exception as e:
        print(e)
        print(f"Malformed GO parameters\n=>{data}")
        abort(400)

    try:
        _ = getCulledVector(taxid, cmin, cmax, fmax)
        print(f"Culled vector found ! [{taxid} {cmin} {cmax} {fmax}]")
    except KeyError : # Culled vector not in cache, build&store
        print(f"Building culled vector... [{taxid} {cmin} {cmax} {fmax}]")
        _ = { # Do we got it all ? Dump it once
            'registry' : taxidVector['registry'],
            'terms' : {  goID : goTerm for goID, goTerm in taxidVector['terms'].items()\
                                                    if len(goTerm['elements']) >= cmin and\
                                                       len(goTerm['elements']) <= cmax and\
                                                       goTerm['freq']          <= fmax \
            }
        }
        storeCulledVector(_, taxid, cmin, cmax, fmax)

    return jsonify(_)

def add_unigo(taxid):
    """ Add a unigo object through client API
        Parameters:
        ---------- 
        taxid: ncbi taxid 
        json payload: ..Univgo.serialize() dict
    """
    try:
        univGoTree = loadUnivGO(request.get_json())
        storeTreeByTaxid(univGoTree, taxid)
        return jsonify({"taxid" : "insertion OK"})
    except KeyError as e:
        print(f"{taxid} already exist in database or malformed request, reject insertion\n=>{e}")
        abort(403)
    except Exception as e:
        print(f"add unigo internal error:{e}")
        abort(500)

def del_unigo(taxid):
    try:
        delTreeByTaxids([taxid])
    except KeyError:
        print(f"{taxid} not found in database, nothing to delete")       
        abort(404) 
  
    return jsonify({"taxid" : "deletion OK"})