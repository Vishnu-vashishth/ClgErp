from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    return render(request, "root/login.html")

def home(request):
    return render(request, "root/home.html")