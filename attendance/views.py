from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    context = {
        "title":"Dashboard"
    }
    return render( request, 'attendance/index.html', context )


def list(request):
    context = {
        "title" : "List"
    }
    return render( request, 'attendance/studentList.html', context )


def fetchStudents(request):
    context = {
        "title" :"Fetch Students"
    }
    return render(request, 'attendance/fetchStudents.html', context)



def show_sub_wise_att(request):
    context = {
        "title" :"Subject Wise Attendance"
    }
    return render(request, 'attendance/show_sub_wise_att.html', context)