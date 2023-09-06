import json
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from ecommerceApp import connector

def index(request):
    return render(request, "polls/index.html")

def cad(request):
    if request.method == "GET":
        return render(request, "polls/cad.html")
    elif request.method == "POST":
        name = request.POST.get("cNome"),
        email= request.POST.get("cEmail")
        password = request.POST.get("cSenha")
        nameStr = ''.join(name)
        data = {"name":f"{nameStr}", "email":email, "password":password}
        connector.post(data)
        return HttpResponse("bala neguim")
    
def login(request):
    if request.method == 'GET':
        return render(request, "polls/login.html")
    else:
        userLogin = request.POST.get("lNome")
        passLogin = request.POST.get("lSenha")
        user = connector.getOne(userLogin)
        jUser = json.loads(user.text)
        if user.status_code == 404:
            invalid = "Usuario ou senhas invalidos"
            invalids = {"invalid":invalid}
            return render(request, 'polls/login.html', invalids)
        elif user.status_code == 200:
            jUser = json.loads(user.text)
            if jUser['password'] == passLogin:
                print(jUser)
                data = {"name": jUser['name'], "email" : jUser['email'], "password": jUser['password'], "logged": "on"}
                print(data)
                connector.put(data, jUser['email'])
                return HttpResponse("platform")
            else:
                return HttpResponse("paia")
        return HttpResponse("paia")    
       
            
        

