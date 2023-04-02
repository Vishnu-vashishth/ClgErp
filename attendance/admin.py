from django.contrib import admin

# Register your models here.

from .models import *

class Agg_AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'attended_classes', 'total_classes', 'status')

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'roll', 'email', 'department', 'password', 'phone', 'otp','department','father_name','mother_name','address','father_phone')

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'sem', 'department')

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'password', 'phone', 'otp')

admin.site.register(Student, StudentAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Agg_Attendance, Agg_AttendanceAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Datewise_Attendance)



