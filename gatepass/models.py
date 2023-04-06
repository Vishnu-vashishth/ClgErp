from django.db import models
import datetime
from attendance.models import *
from twilio.base.exceptions import TwilioRestException
from twilio.rest import Client
import os
from dotenv import load_dotenv
load_dotenv()
def sendsms(phone,msg):
    
    client = Client(os.getenv('Account_SID'), os.getenv('Auth_Token'))

    try:
        message = client.messages.create(
            body=f'{msg}',
            from_=os.getenv('Phone_Number'),
            to=phone
        )
    except TwilioRestException as e:
        print(e)
        return False


class student_requests(models.Model):
    request_id = models.CharField(max_length=100, null=False, unique=True)
    reason = models.CharField(max_length=300, null=False)
    guardian_phone = models.CharField(max_length=11, null=False)
    relation = models.CharField(max_length=100, null=False)
    guardian_name = models.CharField(max_length=100, null=False)
    status = models.CharField(max_length=100, null=False)
    date = models.DateField(auto_now_add=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    cc = models.CharField(max_length=100, null=True )
    hod = models.CharField(max_length=100,null = True)


    def save(self, *args, **kwargs):
      
        Student = self.student
        CC = Roles.objects.get( name = "CC", department = Student.department, semester = self.student.curent_sem, section = self.student.section)
        HOD = Roles.objects.get( name = "HOD", department = Student.department, semester = self.student.curent_sem)
       
        
        if CC : 
            self.cc = CC.teacher.id
            
            if self.status == "Pending" or not self.status:
                teacher = Teacher.objects.get(id = CC.teacher.id)
                x=sendsms(f'+91{teacher.phone}', "Dear CC New request for approval is pending ")
                print(x)
                
        else :
            self.cc = "not found"
           
            
        if  HOD: 
            self.hod = HOD.teacher.id

            
        else :
           
            self.hod = "not found"
        

        if not self.request_id:
            self.request_id = f"{self.student.roll}-{datetime.date.today().strftime('%Y%m%d')}"

        
        super().save(*args, **kwargs)

