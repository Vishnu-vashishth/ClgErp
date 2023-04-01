from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render( request, 'attendance/index.html', {"title":"Dash" } )


def list(request):
    return render( request, 'attendance/studentList.html', {"title":"list" } )


def fetchStudents(request):
    return render(request, 'attendance/fetchStudents.html', {"title":"fetchStudents" })

def show_sub_wise_att(request):
    return render(request, 'attendance/show_sub_wise_att.html', {"title":"show_sub_wise_att" })