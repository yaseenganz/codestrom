from django.urls import path
from . import views
urlpatterns =[
    path('register/',views.PatientRegister, name='patient_register')
]