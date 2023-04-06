from django.shortcuts import render, redirect
import jwt
from django.contrib import messages
from django.conf import settings
from .models import *
from datetime import datetime,timedelta
from datetime import date




def request_gate_pass(request):
    context = {
        'title': 'srequest',
    }
    token = request.COOKIES.get('token')
    if not token:
            messages.error(request, 'You are not logged in')
            return redirect('Login')
    else:
        decoded = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=['HS256'])
        student = Student.objects.get(email=decoded['email'])
        if not student:
            messages.error(request, 'User Not Found')
            return redirect('Login')
        else:
          
          try:
            context['student'] = student.id
            if request.method == 'POST':
                
                reason = request.POST['reason']
                guardian_name = request.POST['guardian_name']
                guardian_phone = request.POST['guardian_phone']
                relation = request.POST['relation']
                rollno = student.roll

                id = f"{rollno}-{date.today().strftime('%Y%m%d')}"

                # request.set_cookie("reqcode", id)
                try:
                    if student_requests.objects.filter(request_id=id).exists():
                        messages.error(request, f'You have already requested for today with id {id} ')
                        return redirect('Login')
                    else:
                        student_request = student_requests(reason=reason, student=student, guardian_name=guardian_name, guardian_phone=guardian_phone, relation=relation,status = 'Pending')
                        student_request.save()
                        smsresult = sendsms(f'+91{guardian_phone}', f'Hey {guardian_name} {student.name} belongs to you and has requested for leave from college with reqid {id}')
                        if not smsresult:
                           smsresult = sendsms(f'+91{student.father_phone}', f'Hey {student.father_name} {student.name} belongs to you and has requested for leave from college with reqid {id}')
                            
                        messages.success( request, f'Your request has been submitted with id {id}')
                        response = redirect('Login')
                        response.set_cookie('reqcode', id)
                        return response
                except Exception as e:
                    messages.error(request, f' {e}')

           
                
       

 
          except Exception as error:
                messages.error(request, f' {error}')
                
                return redirect('request_gate_pass')
    
    context = {  'title': 'srequest','student':student}
    return render(request, 'gatepass/index.html', context)
                














def request_list(request):
    
    token = request.COOKIES.get('token')
    if not token:
            messages.error(request, 'You are not logged in')
            return redirect('Login')
    decoded = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=['HS256'])

    try:
        teacher = Teacher.objects.get(email=decoded['email'])
        role = Roles.objects.get(teacher=teacher).name

        if role == 'HOD':
            requests = student_requests.objects.filter( status ='Approved by cc', hod = teacher.id)

        elif teacher.role == 'CC':
            
            requests = student_requests.objects.filter( status  ='Pending', cc =  teacher.id)

        context = {
            'title': 'Request List',
            'requests': requests,
            'role': role,
            'teacher': teacher
        }
        
        return render(request, 'gatepass/index.html', context)
    
    except  Exception as e:
        messages.error(request, f'Something went wrong {e}')
        return redirect('Login')
    






def approve_request(request,request_id):
    try:
            token = request.COOKIES.get('token')
            if not token:
                messages.error(request, 'You are not logged in')
                return redirect('Login')
            decoded = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=['HS256'])
            if decoded['role'] != 'teacher':
                messages.error(request, 'You are not authorized to access this page')
                return redirect('Login')
            
            teacher = Teacher.objects.get(email=decoded['email'])
            role = Roles.objects.get(teacher=teacher).name
            
            if request.method == 'POST':
                
                req = student_requests.objects.get(request_id=request_id)

                if role == 'CC':
                    req.status = 'Approved by cc'
                    req.save()
                    studentPhone = req.student.phone
                    sendsms(f'+91{studentPhone}', f'Your request with id {req.request_id} has been approved by cc')
                    hodphone =  req.cc.phone
                    smsresult =   sendsms(f'+91{hodphone}', f'Dear HOD request with id {req.request_id} has been approved by cc and is pending your approval. Please login to your account to approve the request.Follow the link https://clggatepasssys-production.up.railway.app/request_list ')
                    print(smsresult)
                    return redirect('request_list')

                elif role == 'HOD':
                    req.status = 'Approved by hod'
                    req.save()
                    studentPhone = req.student.phone
                    sendsms(f'+91{studentPhone}', f'Your request with id {req.request_id} has been approved by hod you can go home now')
                    return redirect('request_list')

                        
                        
                        
                else:
                        messages.error(request, 'something went wrong')
                        return redirect('request_list')
            return redirect('request_list')
    except Exception as e:
        messages.error(request, f'Something went wrong {e}')
        return redirect('request_list')





def reject_request(request,request_id):
    try:
            token = request.COOKIES.get('token')
            if not token:
                messages.error(request, 'You are not logged in')
                return redirect('Login')
            decoded = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=['HS256'])

            if decoded['role'] != 'teacher':
                messages.error(request, 'You are not authorized to access this page')
                return redirect('Login')
            teacher = Teacher.objects.get(email=decoded['email'])
            role = Roles.objects.get(teacher=teacher).name
            if request.method == 'POST':
                req = student_requests.objects.get(request_id=request_id)
                if role == 'CC':
                        req.status = 'Rejected by cc'
                        req.save()
                        # sendsms(f'+91{req.student.phone}', f'Your request with id {req.request_id} has been rejected by cc')
                        return redirect('request_list')

                elif role == 'HOD':
                        req.status = 'Rejected by hod'
                        req.save()
                        sendsms(f'+91{req.student.phone}', f'Your request with id {req.request_id} has been rejected by hod')
                        return redirect('request_list')
            
                else:
                        messages.error(request, 'Invalid request id')
                        return redirect('request_list')
                return redirect('request_list')
    except Exception as e:
        messages.error(request, f'Something went wrong {e}')
        return redirect('request_list')
    





# def trackstat(request):
   
#     if request.method == 'POST':
#         reqid = request.POST['reqid']
#         if student_requests.objects.filter(request_id=reqid).exists():
#             req = student_requests.objects.get(request_id=reqid)
#             return render(request, 'index.html', {'title':'showstatus','req': req.status})
#         else:
#             messages.error(request, 'Invalid request id')
#             return redirect('trackstat')
 
   
#     return render(request, 'gatepass/trackstat.html', { 'title': 'trackstat'})
    
def trackstat(request):
     try:
        token = request.COOKIES.get('token')
        if not token:
                reqid = request.COOKIES.get('reqcode')
                if reqid != None:
                    req = student_requests.objects.get(request_id=reqid)
                    return render(request, 'gatepass/showStatus.html', {'title':'show_status','req': req.status})
                else:  
                    return render (request, 'gatepass/trackStat.html', {'title':'track_stat'})
                
        decoded = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=['HS256'])
        if decoded['role'] == 'student':
            student = Student.objects.get(email=decoded['email'])
            if request.method == 'POST':
                reqid = request.POST['reqid']
                if student_requests.objects.filter(request_id=reqid).exists():
                    req = student_requests.objects.get(request_id=reqid)
                    response = redirect('show_status')
                    response.set_cookie('reqcode', reqid)
                    return response
                else:
                    messages.error(request, 'Invalid request id')
                    return redirect('track_stat')
            else :
                return render(request, 'gatepass/index.html', { 'title': 'track_stat','student':student})       



     except Exception as e:
        messages.error(request, f'Something went wrong {e}')
        return redirect('Login')




def show_status(request):
    try:

        token = request.COOKIES.get('token')
        if not token:
                reqid = request.COOKIES.get('reqcode')
                if reqid != None:
                    req = student_requests.objects.get(request_id=reqid)
                    return render(request, 'gatepass/showStatus.html', {'title':'show_status','req': req.status})
                else:  
                    return redirect('track_stat')
                
        decoded = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=['HS256'])
            
        
            
        if decoded['role'] == 'student':
                    student = Student.objects.get(email=decoded['email'])
                    reqid = request.COOKIES.get('reqcode')
                    if reqid != None:
                        req = student_requests.objects.get(request_id=reqid)
                        return render(request, 'gatepass/index.html', {'title':'show_status','student':student,'req': req})

                    else:  
                        return redirect('track_stat')
                    
                
            

    except Exception as e:
            messages.error(request, f'Something went wrong {e}')
            return redirect('track_stat')






  