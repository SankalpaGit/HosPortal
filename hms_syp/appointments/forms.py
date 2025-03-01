from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Appointment, Patient

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['date', 'time']

        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),  # Calendar Picker
            'time': forms.TimeInput(attrs={'type': 'time'}),  # Time Picker
        }

class PatientRegistrationForm(UserCreationForm):
    class Meta:
        model = Patient
        fields = ['username', 'email', 'phone', 'address', 'password1', 'password2']
