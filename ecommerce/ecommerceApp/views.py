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
        data = {"name":f"{nameStr}", "email":email, "password":password, "logged":"off"}
        connector.post(data)
        return render(request, "polls/login.html")


def platform(request):
    if request.method == 'GET':
        try:
            invalid = "Voce precisa fazer login para continuar"
            invalids = {"invalid":invalid}
            return render(request, 'polls/login.html', invalids)  
        except NameError:
            invalid = "Voce precisa fazer login para continuar"
            invalids = {"invalid":invalid}
            return render(request, 'polls/login.html', invalids)
    else:
        try:
            dataLog['logged'] = "off"
            connector.put(dataLog, jUser['email'])
            return render(request, "polls/login.html")
        except ValueError:
            jUserLog['logged'] = "off"
            connector.put(jUserLog, jUserLog['email'])
            return render(request, "polls/login.html")


def login(request):
    if request.method == 'GET':
        request.session.setdefault("teste", "po")
        print(request.session["teste"])
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
            global jUser
            jUser = json.loads(user.text)
            if jUser['password'] == passLogin:
                global dataLog
                dataLog = {"name":jUser["name"],"email":jUser["email"],"password":jUser["password"],"logged":"on"}
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


       
            
        

