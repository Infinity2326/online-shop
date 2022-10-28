from http.server import HTTPServer
from django.shortcuts import HttpResponse, render
from django.http import HttpResponse


def index(request):
    return render(request, "main/index.html")

def login(request):
    return render(request, "main/login.html")