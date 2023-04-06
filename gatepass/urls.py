from django.urls import path, include

from . import views

urlpatterns = [
    path('request_gate_pass/', views.request_gate_pass, name='request_gate_pass'),
    path('manage_gate_pass/', views.manage_gate_pass, name='manage_gate_pass'),
    path('approve_request/<slug:request_id>/', views.approve_request , name='approve_request'),
    path('reject_request/<slug:request_id>/', views.reject_request , name='reject_request'),
    path('request_list/', views.request_list , name='request_list'),
]
