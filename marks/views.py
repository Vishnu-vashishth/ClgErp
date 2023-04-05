from django.shortcuts import render, redirect
from django.http import HttpResponse
import jwt
from django.contrib import messages
from django.conf import settings
from .models import *
from datetime import datetime
import selenium 
from selenium import webdriver 
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pandas as pd
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')


# Create your views here.

def show_sub_wise_marks(request):
    token = request.COOKIES.get('token')
    if token:
        try:
            decoded = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=['HS256'])
            if decoded['role'] == 'student':
                student = Student.objects.get(email=decoded['email'])
                subjects = Subject.objects.filter(sem=student.curent_sem)
                
                if request.method == 'POST':
                    sub = request.POST.get('subject')
                    ses_index = request.POST.get('sessional_index')
                    if sub == "all" and ses_index == "all":
                        marks = Marks.objects.filter(student=student)
                    elif sub == "all" and ses_index != "all":
                        marks = Marks.objects.filter(student=student, sessional_index=ses_index)
                    elif sub != "all" and ses_index == "all":
                        sub = Subject.objects.get(name=sub)
                        marks = Marks.objects.filter(student=student, subject=sub)
                    else:
                        sub = Subject.objects.get(name=sub)
                        marks = Marks.objects.filter(student=student, subject=sub, sessional_index=ses_index)
                        
                    context = {
                        "title": "Subject Wise Marks",
                        "role": "student",
                        "student": student,
                        "subjects": subjects,
                        "marks": marks
                    }
                else:
                    context = {
                        "title": "Subject Wise Marks",
                        "role": "student",
                        "student": student,
                        "subjects": subjects
                    }

                return render(request, 'marks/index.html', context)
            
            else:
                messages.error(request, 'Invalid Credentials')
                return redirect('Login')

        except Exception as e:
            messages.error(request, f'Something went wrong: {e}')
            return redirect('Login')
            
    else:
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
                      return render( request, 'marks/index.html', context )
                
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
                    return redirect('upload_marks')
                else:
                    messages.error(request, 'Invalid Credentials')
                    return redirect('upload_marks')
            else:
                messages.error(request, 'Invalid Credentials')
                return redirect('upload_marks')
        
        except Exception as e:
            messages.error(request, f'something went wrong{e}')
            return redirect('upload_Marks')


    else :
            messages.error(request, 'Please Login First')
            return redirect('upload_Marks')
     





def seed_univ_result(request):
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
                      result_sem = request.POST.get('result_sem')
                      session = request.POST.get('session')
                    
                      students = Student.objects.filter(department=department, curent_sem=semester, session=session)
                      univ_roll = []

                      for student in students:
                            univ_roll.append(student.univ_roll_no)
                      

                      studentsInfo = []
                      semester = '0'+result_sem
                      driver = webdriver.Chrome(r'C:\Users\vishnu vashishth\Documents\chromedriver_win32\chromedriver.exe', options=chrome_options)
                      
                      for roll_number in univ_roll:
                            try:

                                driver.get("https://jcboseustymca.co.in/Forms/Student/ResultStudents.aspx")

                                # find the input field for roll number
                                roll_no_input = driver.find_element('id','txtRollNo')

                                # enter roll number
                                roll_no_input.send_keys(roll_number)
                                
                                # find the semester dropdown element
                                semester_dropdown = Select(driver.find_element('id','ddlSem'))
                                # select the desired semester
                                semester_dropdown.select_by_value(semester)

                                # find the submit button
                                submit_button = driver.find_element('id','btnResult')

                                # click the submit button

                                submit_button.click()
                                
                                try :
                                    elem= driver.find_element('id','lblMessage')
                                except (ValueError, TypeError):
                                    print("")
                                    continue



                            
                                if elem.text == "No Record Found. Please enter correct roll no or result may not be validate.":
                                    continue

                                driver.get('https://jcboseustymca.co.in/Forms/Student/PrintReportCardNew.aspx')

                                # extract student information
                                name = driver.find_element('id','lblname').text
                                roll_number = driver.find_element('id','lblRollNo').text
                                result = driver.find_element('id','lblResult').text
                                fail = False
                                try:
                                    xxx = float(result)
                                except:
                                    fail = True
                                    
                               
                                sem_field_name = f'sem{semester}'
                                

                                try:
                                  univ_result_instance = univ_result.objects.get(univ_roll_no=roll_number)
                                except univ_result.DoesNotExist:
                                   univ_result_instance = univ_result(univ_roll_no=roll_number)
    
                                setattr(univ_result_instance, sem_field_name, result)
                                univ_result_instance.save()
                                




                                studentsInfo.append({
                                    'name': name,
                                    'roll_number': roll_number,
                                    'result': result,
                                    'fail': fail
                                })
                            except Exception as e:
                                print(e)
                                continue
                       

                    #   df = pd.DataFrame(studentsInfo)
                    #   df.to_excel('senior.xlsx', index="true")
                       
                      driver.quit()
                      context = {
                            "title":"seed univ Marks",
                            "teacher" : teacher,
                            "seme" : semester,
                            "dep" : department,
                            "studentsInfo" : studentsInfo,
                            "departments" : Student.DEPARTMENT_CHOICES,
                            "semester" : Student.SEM_CHOICES,
                            "session" : YEAR_CHOICES

                            }
                      return render( request, 'marks/index.html', context )
                
                else:
   
                        context = {
                                "title":"seed univ Marks",
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