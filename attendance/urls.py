from django.urls import path

from . import views
urlpatterns = [ 
    path('', views.index, name='attendance'),
    path('list/', views.list, name='list'),
    path('fetchStudents/', views.fetchStudents, name='list'),
    path('show_sub_wise_att/', views.show_sub_wise_att, name='show_sub_wise_att'),
]
