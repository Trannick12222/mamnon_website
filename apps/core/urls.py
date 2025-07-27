from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('school-info/', views.api_school_info, name='school_info_api'),
]