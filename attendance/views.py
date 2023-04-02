from django.shortcuts import render, redirect
import jwt
from django.contrib import messages
from django.conf import settings
from .models import *
# Create your views here.


def check_login(request):
    if request.COOKIES.get('token'):
        pass
    else:
     return redirect('Login')

def decode_token(request):
    token = request.COOKIES.get('token')
    decoded = jwt.decode(token,settings.JWT_SECRET_KEY, algorithms=['HS256'])
    return decoded




def index(request):
    token = request.COOKIES.get('token')
    if token:
        try:
            decoded = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=['HS256'])
            if decoded['role'] == 'student':
                student = Student.objects.get(email=decoded['email'])
                context = {
                         "title":"Dashboard",
                         "student" : student
                          }
                return render( request, 'attendance/index.html', context )

            elif decoded['role'] == 'teacher':
                teacher = Teacher.objects.get(email=decoded['email'])
                context = {
                            "title":"Dashboard",
                            "teacher" : teacher
                            }
                return render( request, 'attendance/index.html', context )
             
            else:
                messages.error(request, 'Invalid Credentials')
                return redirect('Login')

        except Exception as e:
            messages.error(request, f'something went wrong{e}')
            return redirect('Login')
            


    else :
            messages.error(request, 'Please Login First')
            return redirect('Login')

    


def profile(request):
    check_login(request)
    decoded = decode_token(request)
    email = decoded['email']
    role = decoded['role']
    context = {
        "title" : "Profile",
        "email" : email,
        "role" : role
    }
    return render( request, 'attendance/index.html', context )










def list(request):
    context = {
        "title" : "List"
    }
    return render( request, 'attendance/index.html', context )


def fetchStudents(request):
    context = {
        "title" :"Fetch Students"
    }
    return render(request, 'attendance/index.html', context)



def show_sub_wise_att(request):
    context = {
        "title" :"Subject Wise Attendance"
    }
    return render(request, 'attendance/index.html', context)