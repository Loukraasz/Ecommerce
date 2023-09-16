import json
import requests

def getOne(email):
    return requests.get(f"http://localhost:8080/ecUser/{email}")
def getAll():
    return requests.get("http://localhost:8080/ecUser")
def post(data):
    requests.post("http://localhost:8080/ecUserPost", data=json.dumps(data), headers={"Content-Type":"application/json"})
def put(data, email):
    requests.put(f"http://localhost:8080/ecUserPut/{email}", data=json.dumps(data), headers={"Content-Type":"application/json"})
def delete(email):
    requests.delete(f"http://localhost:8080/ecUserDelete/{email}")
def getSid(sessionId):
    return requests.get(f"http://localhost:8080/ecUserSID/{sessionId}")

