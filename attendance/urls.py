from django.urls import path

from . import views
urlpatterns = [
    path('attendance', views.index, name='index'),
    path('attendance/list', views.list, name='index'),
]
