from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    context = {
        "title": "Login"}
    return render(request, "root/index.html",context =  context)

def home(request):
    context = {
        "title": "Home"}
    return render(request, "root/index.html",context =  context)

def reset(request):
    context = {
        "title": "Reset"}
    return render(request, "root/index.html",context =  context)

def forgot(request):
    context = {
        "title": "Forgot"}
    return render(request, "root/index.html",context =  context)