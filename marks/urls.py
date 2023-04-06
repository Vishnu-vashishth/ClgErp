from django.urls import path, include

from . import views
urlpatterns = [ 
    path('show_sub_wise_marks/', views.show_sub_wise_marks, name='show_sub_wise_marks'),
    path('upload_marks/', views.upload_marks, name='upload_marks'),
    path('save_marks/', views.save_marks, name='save_marks'),
    path('seed_univ_result/', views.seed_univ_result, name='seed_univ_result'),
    path('show_univ_result/', views.show_univ_result, name='show_univ_result'),
]