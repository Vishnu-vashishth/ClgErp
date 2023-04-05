

from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('attendance/',include('attendance.urls')),
    path('marks/',include('marks.urls')),
    path('login/',views.login,name='Login'),
    path('',views.home,name='Home'),
    path('reset/',views.reset,name='Reset'),
    path('forgot/',views.forgot,name='Forgot'),
    path('logout/',views.logout,name='Logout'),
]
