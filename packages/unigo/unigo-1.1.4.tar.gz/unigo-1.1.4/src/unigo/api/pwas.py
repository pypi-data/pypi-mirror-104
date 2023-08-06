from flask import Flask, abort, jsonify, request
import requests, json
from marshmallow import EXCLUDE
from .. import vloads as createGOTreeTestUniverseFromAPI
from .. import uloads as createGOTreeTestFromAPI
from .. import utils
from .io import checkPwasInput
from ..stat_utils import applyOraToVector, kappaClustering
from .data_objects import CulledGoParametersSchema as goParameterValidator

GOPORT=1234
GOHOST="127.0.0.1"
def listen(goApiHost:str, goApiPort:int, vectorized:bool):
    global GOPORT, GOHOST
    GOPORT = goApiPort
    GOHOST = goApiHost

    app = Flask(__name__)
    app.add_url_rule("/", 'hello', hello)
    if vectorized:
        print(f"PWAS API vector listening")
        app.add_url_rule("/compute", "computeOverVector", computeOverVector, methods=["POST"])
    else:
        print(f"PWAS API tree listening")
        app.add_url_rule("/compute", "computeOverTree", computeOverTree, methods=["POST"])
    return app

def hello():
    return "Hello pwas"

def computeOverVector():
    forceUniversal = False
    data = checkPwasInput()
   
    print(f'I get data with {len(data["all_accessions"])} proteins accessions including {len(data["significative_accessions"])} significatives')
    
    if forceUniversal:
        go_resp = utils.unigo_vector_from_api(GOHOST, GOPORT, data["taxid"])
    else:
         # Culling vector parameters
        _goParameterValidator = goParameterValidator()
        goParameter = _goParameterValidator.load(request,  unknown=EXCLUDE)
        go_resp = utils.unigo_culled_from_api(GOHOST, GOPORT, data["taxid"], goParameter)

    if go_resp.status_code != 200:
        print(f"ERROR request returned {go_resp.status_code}")
        abort(go_resp.status_code)
    
    vectorizedProteomeTree = json.loads(go_resp.text)
    #print(vectorizedProteomeTree)

    res = applyOraToVector(vectorizedProteomeTree, data["all_accessions"], data["significative_accessions"], 0.05)
    print(f"clustering {len(res.keys())} GO terms")
    #print("NO Clustering")
    #return jsonify(res)
    Z = kappaClustering(vectorizedProteomeTree["registry"], res)

    return jsonify(Z)

def computeOverTree():
    data = checkPwasInput() 
    print(f'I get data with {len(data["all_accessions"])} proteins accessions including {len(data["significative_accessions"])} significatives')

    go_resp = utils.unigo_tree_from_api(GOHOST, OPORT, data["taxid"])

    if go_resp.status_code != 200:
        print(f"ERROR request returned {go_resp.status_code}")
        abort(go_resp.status_code)
    
    print("Create Unigo tree")
    unigoTreeFromAPI = createGOTreeTestFromAPI(go_resp.text, data["all_accessions"])
    x,y = unigoTreeFromAPI.dimensions
    print("Unigo Object successfully buildt w/ following dimensions:")
    print(f"\txpTree => nodes:{x[0]} children_links:{x[1]}, total_protein_occurences:{x[2]}, protein_set:{x[3]}")  
    print(f"\t universeTree => nodes:{y[0]} children_links:{y[1]}, total_protein_occurences:{y[2]}, protein_set:{y[3]}")  

    #Compute fisher stats
    if data["method"] == "fisher":
        print("Computing ORA with fisher")
        rankingsORA = unigoTreeFromAPI.computeORA(data["significative_accessions"], verbose = False)
        
        return rankingsORA.json

    return {"not computed": "unavailable stat method"}

