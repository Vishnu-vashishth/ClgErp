from django.shortcuts import render,redirect
from django.contrib.auth.hashers import check_password
from attendance.models import *
import jwt
from django.conf import settings
from django.core.mail import send_mail
import random
from dotenv import load_dotenv
import os
from django.contrib import messages
load_dotenv()


def home(request):
    context = {
        "title": "Home"}
    return render(request, "root/index.html",context =  context)





def login(request):
    context = {
        "title": "Login"}
    token = request.COOKIES.get('token')
    if token:
            try:  
                decoded = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
                student = Student.objects.get(email = decoded)
                if student:
                    return redirect('attendance')
                else:
                    teacher = Teacher.objects.get(eamil = decoded)
                    if teacher: 
                      return redirect('attendance')
            except:
                pass

    if request.method == 'POST':
        email = request.POST["email"]
        password = request.POST["password"]
        role = request.POST["role"]
        if role == "student":
            try :
                student = Student.objects.get(email = email)
                if check_password(password,student.password):
                    encode = jwt.encode({'email': email}, settings.SECRET_KEY, algorithm='HS256')
                    response = redirect('attendance')
                    response.set_cookie('token', encode)
                    messages.success(request, 'Login Successfully')
                    return response
                else:
                    messages.error(request, 'Invalid Credentials')
                    return redirect('Login')
            except:
                messages.error(request, 'something went wrong')
                return redirect('Login')
            
        elif role == "teacher":
            try :
                teacher = Teacher.objects.get(email = email)
                if check_password(password,teacher.password):
                    encode = jwt.encode({'email': email}, settings.SECRET_KEY, algorithm='HS256')
                    response = redirect('attendance')
                    response.set_cookie('token', encode)
                    messages.success(request, 'Login Successfully')
                    return response
                    
                else:
                    messages.error(request, 'Invalid Credentials')
                    return redirect('Login')
            except:
                messages.error(request, 'something went wrong')
                return redirect('Login')

    return render(request, "root/index.html",context =  context)




def reset(request):
    context = {
        "title": "Reset"}
    try:
       if request.method == 'POST':
            email = request.POST["email"]
            otp = request.POST["otp"]
            password = request.POST["password"]
            student = Student.objects.get(email = email)
            if student:
                if otp == student.otp and otp != None :
                    student.password = password
                    student.otp = None
                    student.save()
                    messages.success(request, 'Password Reset Successfully')
                    return redirect('Login')
                else:
                    messages.error(request, 'Invalid Otp')
                    return redirect('Login')
            else:
                teacher = Teacher.objects.get(email = email)
                if teacher:
                    if otp == teacher.otp:
                        teacher.password = password
                        teacher.otp = None
                        teacher.save()
                        messages.success(request, 'Password Reset Successfully')
                        return redirect('Login')
                    else:
                        messages.error(request, 'Invalid Otp')
                        return redirect('Login')
                else:
                    messages.error(request, 'Wrong Email')
                    return redirect('Login')
        
    except:
        messages.error(request, 'something went wrong')
        return redirect('Login')
    
    return render(request, "root/index.html",context =  context)




def forgot(request):
    context = {
        "title": "Forgot"}
    if request.method == 'POST':
        email = request.POST["email"]
        if email:
            try:
                student = Student.objects.get(email = email)
                if student :
                    
                    otp = random.randint(100000,999999)
                    student.otp = otp
                    student.save()
                    subject = 'Password Reset'
                    message = f"Your Password reset otp is {otp}"

                    recipient_list = [email]
                    send_mail(subject, message, "helpFrom@satyug.edu.in", recipient_list, fail_silently=False, auth_user=None, auth_password=None, connection=None, html_message=None)
                    messages.success(request, 'Otp sent to your email')
                    return redirect('Login')
                else:
                    teacher = Teacher.objects.get(email = email)
                    if teacher:
                        otp = random.randint(100000,999999)
                        teacher.otp = otp
                        teacher.save()

                        subject = 'Password Reset'
                        message = f"Your Password reset otp is {otp}"
                        recipient_list = [email]
                        send_mail(subject, message, "helpFrom@satyug.edu.in", recipient_list, fail_silently=False, auth_user=None, auth_password=None, connection=None, html_message=None)
                        messages.success(request, 'Otp sent to your email')
                        return redirect('Login')
                    else:
                        messages.error(request, 'invalid Email')
                        return redirect('forgot')
            except:
                messages.error(request, 'something went wrong')
                return redirect('Login')
            
    return render(request, "root/index.html",context =  context)