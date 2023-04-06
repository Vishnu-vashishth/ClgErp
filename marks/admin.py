from django.contrib import admin
from .models import *
# Register your models here.

class MarksAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'sessional_index', 'marks_obtained', 'max_marks')

class univ_resultAdmin(admin.ModelAdmin):
    list_display = ('student', 'univ_roll_no', 'sem01', 'sem02', 'sem03', 'sem04', 'sem05', 'sem06', 'sem07', 'sem08')

admin.site.register(Marks, MarksAdmin)
admin.site.register(univ_result, univ_resultAdmin)