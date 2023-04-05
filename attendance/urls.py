from django.urls import path

from . import views
urlpatterns = [ 
    path('', views.index, name='attendance'),
    path('profile', views.profile, name='profile'),
    
    path('show_sub_wise_att/', views.show_sub_wise_att, name='show_sub_wise_att'),
    path('markAttendance/', views.markAttendance, name='markAttendance'),
    path('saveAttendance/', views.saveAttendance, name='saveAttendance'),
    path('view_date_wise_attendance/', views.view_date_wise_attendance, name='view_date_wise_attendance'),
]
