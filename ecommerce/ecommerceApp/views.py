import json
from django.http import HttpResponse
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
        if user.status_code == 404:
            return HttpResponse("paiaUser")
        elif user.status_code == 200:
            jUser = json.loads(user.text)
            if jUser['password'] == passLogin:
                return HttpResponse("descubra")
            else:
                return HttpResponse("paia")
       
            
        

