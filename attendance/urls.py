from django.urls import path

from . import views
urlpatterns = [
    path('att/', views.index, name='index'),
]
