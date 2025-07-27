from django.urls import path
from . import views

app_name = 'schools'

urlpatterns = [
    path('classes/', views.class_list, name='class_list'),
    path('teachers/', views.teacher_list, name='teacher_list'),
]