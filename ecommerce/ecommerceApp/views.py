import json
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from ecommerceApp import connector
from ecommerceApp import sendEmail

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
        return render(request, "polls/login.html")
    
def platform(request):
    return render(request, "polls/platform.html")

    
def login(request):
    if request.method == 'GET':
        return render(request, "polls/login.html")
    else:
        userLogin = request.POST.get("lNome")
        passLogin = request.POST.get("lSenha")
        user = connector.getOne(userLogin)
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
            
def passwordChange(request):
    if request.method == 'GET':
        return render(request, 'polls/passwordChange.html')
    else:
        global userPassLogin
        userPassLogin = request.POST.get("lNome")
        user = connector.getOne(userPassLogin)
        if user.status_code == 404:
            emailInvalid = "email nao existente"
            emailInvalids = {'emailInvalid':emailInvalid}
            return render(request, "polls/passwordChange.html", emailInvalids)
        elif user.status_code == 200:
            sendEmail.sendEmails(userPassLogin)
            return render(request, 'polls/confirmedEmail.html')
            
def confirmedEmail(request):
    if request.method == "GET":
        return render(request, 'polls/confirmedEmail.html')
    else:
        codeValidate = request.POST.get("validateCode")
        if codeValidate == sendEmail.final:
            return render(request, "polls/newPassword.html")
        elif codeValidate != sendEmail.final:
            errorCode = "Codigo Invalido"
            errorCodes = {"errorCode":errorCode}
            return render(request, 'polls/confirmedEmail.html', errorCodes)  
       
                  
def newPassword(request):
    if request.method == "GET":
        return render(request, "polls/newPassword.html")
    else:
        np = request.POST.get("newPassword")
        print(userPassLogin)
        
       
            
        

