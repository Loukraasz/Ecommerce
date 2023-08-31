import json
import requests
import t

r = requests.get("http://localhost:8080/ecProd")

data =  {"stock": 20, "name":"camisa", "price": 29.90,"category":"fu"}

p = requests.post("http://localhost:8080/ecProd", data=json.dumps(data), headers={"Content-Type":"application/json"})

print(r.text)

