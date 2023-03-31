

from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('attendance.urls')),
    path('login/',views.login,name='Login'),
    path('',views.home,name='Home'),
]
