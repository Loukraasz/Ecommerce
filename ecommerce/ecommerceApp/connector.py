import json
import requests

def getAll():
    return requests.get("http://localhost:8080/ecProd")
def post(data):
    requests.post("http://localhost:8080/ecProd", data=json.dumps(data), headers={"Content-Type":"application/json"})



