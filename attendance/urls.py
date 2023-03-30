from django.urls import path

from . import views
urlpatterns = [
    path('atten', views.index, name='index'),
]
