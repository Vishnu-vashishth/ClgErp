from django.shortcuts import render, redirect
from django.http import HttpResponse
import jwt
from django.contrib import messages
from django.conf import settings
from .models import *
from datetime import datetime
# Create your views here.

def show_sub_wise_marks(request):
     token = request.COOKIES.get('token')
     if token:
        try:
            decoded = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=['HS256'])
            if decoded['role'] == 'student':
                student = Student.objects.get(email=decoded['email'])
                subjects = Subject.objects.filter(sem=student.curent_sem)
                context = {
                         "title":"Subject Wise Marks",
                         "role" : "student",
                         "student":student,
                         "subjects" : subjects
                          }
                
                if request.method == 'POST':
                    sub = request.POST.get('subject')
                    ses_index = request.POST.get('sessional_index')
                    if sub == "all" and ses_index == "all":
                        # attendance = Agg_Attendance.objects.filter(student=student)
                        marks= Marks.objects.filter(student=student)
                    elif sub == "all" and ses_index != "all":
                        marks= Marks.objects.filter(student=student, sessional_index=ses_index)
                    elif sub != "all" and ses_index == "all":
                        sub = Subject.objects.get(name=sub)
                        marks= Marks.objects.filter(student=student, subject=sub)
                    else:
                        sub = Subject.objects.get(name=sub)
                        marks= Marks.objects.filter(student=student, subject=sub, sessional_index=ses_index)
                    context = {
                         "title":"Subject Wise Marks",
                         "role" : "student",
                         "student" : student,
                         "subjects" : subjects,
                         "marks" : marks
                          }
                    return render( request, 'attendance/index.html', context )
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
     
     
def upload_marks(request):
    token = request.COOKIES.get('token')
    if token:
        try:
            decoded = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=['HS256'])
            current_year = datetime.now().year
            YEAR_CHOICES = [year for year in range(current_year-5, current_year+1)]
            if decoded['role'] == 'teacher':
                teacher = Teacher.objects.get(email=decoded['email'])
                if request.method == 'POST':
                      department = request.POST.get('department')
                      semester = request.POST.get('semester')
                      section = request.POST.get('section')
                      session = request.POST.get('session')
                      students = Student.objects.filter(department=department,section=section, curent_sem=semester, session=session)
                    #   students = Student.objects.filter(department=department, curent_sem=semester)
                      subjects = Subject.objects.filter(sem=semester)
                      context = {
                            "title":"Upload Marks",
                            "teacher" : teacher,
                            "students" : students,
                            "subjects" : subjects,
                            "departments" : Student.DEPARTMENT_CHOICES,
                            "semester" : Student.SEM_CHOICES,
                            "session" : YEAR_CHOICES

                            }
                      return render( request, 'attendance/index.html', context )
                
                else:
                       

                        
                        
                        context = {
                                "title":"Upload Marks",
                                "teacher" : teacher,
                                "departments" : Student.DEPARTMENT_CHOICES,
                                "semester" : Student.SEM_CHOICES,
                                "session" : YEAR_CHOICES
                                }
                        
                        return render( request, 'marks/index.html', context )

                    
            
            else:
                messages.error(request, 'Invalid Credentials')
                return redirect('Login')
        
        except Exception as e:
            messages.error(request, f'something went wrong{e}')
            return redirect('Login')


    else :
            messages.error(request, 'Please Login First')
            return redirect('Login')


def save_marks(request):
    token = request.COOKIES.get('token')
    if token:
        try:
            decoded = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=['HS256'])
            if decoded['role'] == 'teacher':
                teacher = Teacher.objects.get(email=decoded['email'])
                if request.method == 'POST':
                    student = request.POST.getlist('student')
                    subject = request.POST.getlist('subject')
                    sessional_index = request.POST.getlist('sessional_index')
                    marks_obtained = request.POST.getlist('marks_obtained')
                    max_marks = request.POST.getlist('max_marks')
                    for i in range(len(student)):
                        student = Student.objects.get(id=student[i])
                        subject = Subject.objects.get(id=subject[i])
                        marks = Marks.objects.create(student=student, subject=subject, sessional_index=sessional_index[i], marks_obtained=marks_obtained[i], max_marks=max_marks[i])
                        marks.save()
                    messages.success(request, 'Marks Uploaded Successfully')
                    return redirect('/')
                else:
                    messages.error(request, 'Invalid Credentials')
                    return redirect('Upload_Marks')
            else:
                messages.error(request, 'Invalid Credentials')
                return redirect('Upload_Marks')
        
        except Exception as e:
            messages.error(request, f'something went wrong{e}')
            return redirect('Upload_Marks')


    else :
            messages.error(request, 'Please Login First')
            return redirect('Upload_Marks')
     