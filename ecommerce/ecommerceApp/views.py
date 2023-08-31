from django.shortcuts import render

def index(request):
    return render(request, "polls/index.html")
def cad(request):
    return render(request, "polls/cad.html")
def login(request):
    return render(request, "polls/login.html")

