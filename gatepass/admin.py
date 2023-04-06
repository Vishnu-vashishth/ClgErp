from django.contrib import admin
from .models import *
# Register your models here.
class student_requestsAdmin(admin.ModelAdmin):
    list_display = ('request_id','reason','guardian_name','guardian_phone','relation','student','status','date','cc','hod')

admin.site.register(student_requests,student_requestsAdmin)
