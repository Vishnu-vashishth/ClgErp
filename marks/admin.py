from django.contrib import admin
from .models import Marks
# Register your models here.

class MarksAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'sessional_index', 'marks_obtained', 'max_marks')

admin.site.register(Marks, MarksAdmin)