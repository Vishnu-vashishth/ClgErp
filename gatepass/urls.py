from django.urls import path, include

from . import views

urlpatterns = [
    path('request_gate_pass/', views.request_gate_pass, name='request_gate_pass'),
    path('request_list/', views.request_list, name='request_list'),
    path('approve_request/<slug:request_id>/', views.approve_request , name='approve_request'),
    path('reject_request/<slug:request_id>/', views.reject_request , name='reject_request'),
    path('request_list/', views.request_list , name='request_list'),
    path('show_status/', views.show_status , name='show_status'),
    path('track_stat/', views.trackstat , name='track_stat'),
]
