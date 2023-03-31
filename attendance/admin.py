from django.contrib import admin

# Register your models here.

from .models import Student, Subject, Agg_Attendance

admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Agg_Attendance)


