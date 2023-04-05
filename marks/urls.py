from django.urls import path, include

from . import views
urlpatterns = [ 
    path('show_sub_wise_marks/', views.show_sub_wise_marks, name='show_sub_wise_marks'),
    path('upload_marks/', views.upload_marks, name='upload_marks'),
    path('save_marks/', views.save_marks, name='save_marks'),
]