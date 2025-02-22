from django.shortcuts import render
from django.contrib.auth import get_user_model
from .forms import PatientForm
User = get_user_model()

def PatientRegister(request):
    form = PatientForm()
    context={
        'title':"SignUp",
        'form':form
    }
    return render(request,'index.html',context=context)