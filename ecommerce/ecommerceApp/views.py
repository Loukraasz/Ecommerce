from django.http import HttpResponse
from django.shortcuts import render
from ecommerceApp import connector

def index(request):
    return render(request, "polls/index.html")

def cad(request):
    if request.method == "GET":
        return render(request, "polls/cad.html")
    elif request.method == "POST":
        p = request.POST.get("cNome"),
        x= request.POST.get("cEmail")
        c = request.POST.get("cSenha")
        p2 = ''.join(p)
        print(f"{p2}")
        data = {"name":f"{p2}", "stock":90, "category":"anto", "price":90.20}
        connector.post(data)
        return HttpResponse("bala neguim")
    
def login(request):
    return render(request, "polls/login.html")

