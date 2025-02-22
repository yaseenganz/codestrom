from django import forms
from .models import PatientProfile

class PatientForm(forms.ModelForm):
    class Meta:
        model = PatientProfile
        fields = '__all__'
