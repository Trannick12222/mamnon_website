from django.urls import path
from . import views

app_name = 'contacts'

urlpatterns = [
    path('', views.contact_page, name='contact'),
    path('form/', views.contact_form, name='contact_form'),
]