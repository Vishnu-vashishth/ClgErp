from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render( request, 'attendance/index.html', {"title":"Dash" } )


def list(request):
    return render( request, 'attendance/studentList.html', {"title":"list" } )