from django.db import models

from attendance.models import *


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

