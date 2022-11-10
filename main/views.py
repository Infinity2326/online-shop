from http.server import HTTPServer

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import HttpResponse, render, redirect
from django.http import HttpResponse
from django.db import models
from django.contrib import messages
from .forms import UserRegisterForm



def index(request):
    return render(request, "main/index.html")

def login(request):
    return render(request, "main/login.html")

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Вы успешно зарегестрировались')
            return redirect('login')
        else:
            messages.error(request,'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'main/register.html',{"form":form})
