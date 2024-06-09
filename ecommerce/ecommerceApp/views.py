import json
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from requests import JSONDecodeError
import requests
from ecommerceApp import connector
from ecommerceApp import sendEmail


def cad(request):
    if request.method == "GET":
        return render(request, "polls/cad.html")
    else:
        name = request.POST.get("cNome"),
        email= request.POST.get("cEmail")
        password = request.POST.get("cSenha")
        confPass = request.POST.get("cConfSenha")
        nameStr = ''.join(name)
        data = {"name":f"{nameStr}", "email":email, "password":password, "sessionId":"."}
        emailExists = connector.getOne(email).status_code
        passLength = password.__len__()
        nameLength = nameStr.__len__()
        if emailExists == 404 and email != "" and nameLength > 3 and passLength >=8 and confPass == password:
            connector.post(data)
            return render(request, "polls/login.html")
        else:
            error = "Email Ja Existente ou Invalido" 
            errorEmail = {"errorEmail":error}
            return render(request, "polls/cad.html",context=errorEmail)
        
        
        
        


def platform(request):
    if request.method == 'GET':
            sessionUser = request.COOKIES.get("sessionid")
            userSession = connector.getSid(sessionUser)
            if not userSession:
                invalid = "Voce precisa fazer login para continuar"
                invalids = {"invalid":invalid}
                return render(request, 'polls/login.html', invalids)
            else:
                jUserSession = json.loads(userSession.text)
                if jUserSession["sessionId"] == sessionUser:
                    return render(request, "polls/platform.html")
                else:
                    invalid = "Voce precisa fazer login para continuar"
                    invalids = {"invalid":invalid}
                    return render(request, 'polls/login.html', invalids)      
    else:
        sessionUser = request.COOKIES.get("sessionid")
        userSession = connector.getSid(sessionUser)
        jUserSession = json.loads(userSession.text)
        if jUserSession["sessionId"] == sessionUser:
            dataLog = {"name":jUserSession["name"],"email":jUserSession["email"],"password":jUserSession["password"],"sessionId":"."}
            connector.put(dataLog, jUserSession['email'])
            return render(request, "polls/login.html")


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
            request.session["session"] = userLogin
            global jUser
            jUser = json.loads(user.text)
            global sessionUser
            sessionUser = request.COOKIES.get("sessionid")
            if jUser['password'] == passLogin:
                global dataLog
                dataLog = {"name":jUser["name"],"email":jUser["email"],"password":jUser["password"],"sessionId":sessionUser}
                connector.put(dataLog, jUser['email'])
                return render(request, "polls/platform.html")
            else:
                invalid = "Usuario ou senhas invalidos"
                invalids = {"invalid":invalid}
                return render(request, 'polls/login.html', invalids)
            
                
            
def passwordChange(request):
    if request.method == 'GET':
        return render(request, 'polls/passwordChange.html')
    else:
        global userPassLogin
        userPassLogin = request.POST.get("recEmail")
        user = connector.getOne(userPassLogin)
        if user.status_code == 404:
            emailInvalid = "email nao existente"
            emailInvalids = {'emailInvalid':emailInvalid}
            return render(request, "polls/passwordChange.html", emailInvalids)
        elif user.status_code == 200:
            print(userPassLogin)
            sendEmail.sendEmails(userPassLogin)
            return render(request, 'polls/confirmedEmail.html')
            
def confirmedEmail(request):
    if request.method == "GET":
        try:
            if userPassLogin != None:
                return render(request, "polls/newPassword.html")
            else:
                emailInvalid = "primeiro, informe seu email"
                emailInvalids = {'emailInvalid':emailInvalid}
                return render(request, "polls/passwordChange.html", emailInvalids)
        except NameError:
                emailInvalid = "primeiro, informe seu email"
                emailInvalids = {'emailInvalid':emailInvalid}
                return render(request, "polls/passwordChange.html", emailInvalids)
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
        try:
            if userPassLogin != None:
                return render(request, "polls/newPassword.html")
            else:
                emailInvalid = "primeiro, informe seu email"
                emailInvalids = {'emailInvalid':emailInvalid}
                return render(request, "polls/passwordChange.html", emailInvalids)
        except NameError:
                emailInvalid = "primeiro, informe seu email"
                emailInvalids = {'emailInvalid':emailInvalid}
                return render(request, "polls/passwordChange.html", emailInvalids)
    else:
        np = request.POST.get("newPassword")
        user = connector.getOne(userPassLogin)
        jUser = json.loads(user.text)
        data = {"name":jUser['name'], "email":jUser['email'], "password": np , "logged":"off"}
        connector.put(data, jUser['email'])
        return render(request, "polls/login.html")
    
def log(request):
    if request.method == "GET":
        return render(request, "polls/log.html")
    else:
        userL = request.POST.get("lNome")
        user = connector.getOne(userL)
        if user.status_code == 404:
            invalid = "email invalidos"
            invalids = {"invalid":invalid}
            return render(request, 'polls/log.html', invalids)
        elif user.status_code == 200:
            global jUserLog
            jUserLog = json.loads(user.text)
            if jUserLog['logged'] == "off":
                invalid = "Entre novamente"
                invalids = {"invalid":invalid}
                return render(request, 'polls/log.html', invalids)
            elif jUserLog["logged"] == "on":
                return render(request, "polls/platform.html")
            
         


def court(request):
    return render(request, "polls/court.html")
def max(request):
    return render(request, "polls/max.html")
def revolution(request):
    return render(request, "polls/revolution.html")
def excee(request):
    return render(request, "polls/excee.html")
def downshifter(request):
    return render(request, "polls/downshifter.html")
def court_specs(request):
    return render(request, "polls/court_specs.html")
def downshifter_specs(request):
    return render(request, "polls/downshifter_specs.html")
def excee_specs(request):
    return render(request, "polls/excee_specs.html")
def revolution_specs(request):
    return render(request, "polls/revolution_specs.html")
def max_specs(request):
    return render(request, "polls/max_specs.html")


       
            
        

