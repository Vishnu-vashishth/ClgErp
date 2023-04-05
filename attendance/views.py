from django.shortcuts import render, redirect
from django.http import HttpResponse
import jwt
from django.contrib import messages
from django.conf import settings
from .models import *
from datetime import datetime,timedelta
from datetime import date
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
                         "role" : "student",
                         "student":student
                          }
                return render( request, 'attendance/index.html', context )

            elif decoded['role'] == 'teacher':
                teacher = Teacher.objects.get(email=decoded['email'])
                context = {
                            "title":"Dashboard",
                            "role" : "teacher",
                            "teacher": teacher
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
     token = request.COOKIES.get('token')
     if token:
        try:
            decoded = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=['HS256'])
            if decoded['role'] == 'student':
                student = Student.objects.get(email=decoded['email'])
                context = {
                         "title":"Profile",
                         "student" : student
                          }
                return render( request, 'attendance/index.html', context )

            elif decoded['role'] == 'teacher':
                teacher = Teacher.objects.get(email=decoded['email'])
                context = {
                            "title":"Profile",
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










def list(request):
    context = {
        "title" : "List"
    }
    return render( request, 'attendance/index.html', context )


def fetchStudents(request):
    context = {
        "title" :"Fetch Students",
        
    }
    return render(request, 'attendance/index.html', context)






def show_sub_wise_att(request):
     token = request.COOKIES.get('token')
     if token:
        try:
            decoded = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=['HS256'])
            if decoded['role'] == 'student':
                student = Student.objects.get(email=decoded['email'])
                subjects = Subject.objects.filter(sem=student.curent_sem)
                context = {
                         "title":"Subject Wise Attendance",
                         "role" : "student",
                         "student":student,
                         "subjects" : subjects
                          }
                
                if request.method == 'POST':
                    sub = request.POST.get('subject')
                    if sub == "all":
                        attendance = Agg_Attendance.objects.filter(student=student)
                    else:
                        sub = Subject.objects.get(name=sub)
                        attendance = Agg_Attendance.objects.filter(student=student, subject=sub)
                    context = {
                         "title":"Subject Wise Attendance",
                         "role" : "student",
                         "student" : student,
                         "subjects" : subjects,
                         "attendance" : attendance
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





def markAttendance(request ) :
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
                            "title":"Mark Attendance",
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
                                "title":"Mark Attendance",
                                "teacher" : teacher,
                                "departments" : Student.DEPARTMENT_CHOICES,
                                "semester" : Student.SEM_CHOICES,
                                "session" : YEAR_CHOICES
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
    





def saveAttendance(request):
    # current_year = datetime.now().year
    # YEAR_CHOICES = [year for year in range(current_year-5, current_year+1)]
    token = request.COOKIES.get('token')
    if token:

        decoded = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=['HS256'])
        if decoded['role'] == 'teacher':
            teacher = Teacher.objects.get(email=decoded['email'])
            if request.method == 'POST':
                    try:
                        selected_subject = request.POST.get('subject')
                        students_present = request.POST.getlist('attendance[]')
                        date_str = request.POST.get('current_date')
                        print(date_str)
                        date_obj = date.fromisoformat(date_str) 
                        print(date_obj)
                        subject = Subject.objects.get(name=selected_subject)
                        
                        # Get the session value from any of the students present in the list
                        student_id = students_present[0] # get the first student ID
                        student = Student.objects.get(id=student_id)
                        session = student.session
                        section = student.section

                        total_attendance_obj, created = total_attendance.objects.get_or_create(subject=subject, session=session,section = section)
                        total_attendance_obj.total_classes += 1

                        total_attendance_obj.save()

                        for student_id in students_present:
                            student = Student.objects.get(id=student_id)
                            attendance, created = Agg_Attendance.objects.get_or_create(student=student, subject=subject)
                            attendance.attended_classes += 1
                            attendance.status = 'P'
                            attendance.save()


                            datewise_attendance, created = Datewise_Attendance.objects.get_or_create(student=student, date=date_obj)
                            datewise_attendance.present_in.add(subject)

                        messages.success(request, 'Attendance submitted successfully.')
                        return redirect('markAttendance')
                    except Subject.DoesNotExist:
                        messages.error(request, 'Invalid subject selected.')
                    except Student.DoesNotExist:
                        messages.error(request, 'Invalid student selected.')
                    except Exception as e:
                        messages.error(request, 'An error occurred while processing the request: {}'.format(str(e)))
                        
    messages.success(request, 'Attendance submitted successfully.')
    return redirect('markAttendance')



def view_date_wise_attendance(request):
    token = request.COOKIES.get('token')
    if token:
        try:
            decoded = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=['HS256'])
            if decoded['role'] == 'student':
                student = Student.objects.get(email=decoded['email'])

                if request.method == 'POST':
                    start_date = request.POST.get('start_date')
                    end_date = request.POST.get('end_date')

                    start = date.fromisoformat(start_date)
                    end = date.fromisoformat(end_date)
                    
                    delta = timedelta(days=1)
                    dates = []
                    while start <= end:
                            dates.append(start)
                            start += delta

                    attendance_data = []

                    for datee in dates:
                        attendance = Datewise_Attendance.objects.prefetch_related('present_in').filter(date=datee,student= student).values_list('present_in__name', flat=True)
                        if attendance:
                           attendance_data.append({'datee': datee, 'subjectList': attendance})

                    context = { 'title': 'View Attendance','student': student,'attendance_data': attendance_data}
                    return render(request, 'attendance/index.html', context)

                else:
                    context = {
                        'title': 'View Attendance',
                        'student': student

                    }
                    return render(request, 'attendance/index.html', context)
            
             
            else:
                messages.error(request, 'Invalid Credentials')
                return redirect('Login')

        except Exception as e:
            messages.error(request, f'{e}')
            return redirect('view_date_wise_attendance')
            
    else :
            messages.error(request, 'Please Login First')
            return redirect('Login')