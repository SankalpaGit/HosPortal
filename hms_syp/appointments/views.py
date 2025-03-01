from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Doctor, Appointment
from .forms import AppointmentForm, PatientRegistrationForm

def home(request):
    return render(request, 'Home.html')

@login_required
def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctor_list.html', {'doctors': doctors})

@login_required
def book_appointment(request, doctor_id):
    doctor = Doctor.objects.get(id=doctor_id)
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = request.user
            appointment.doctor = doctor
            appointment.is_approved = True  # Auto-approved for now
            appointment.save()
            return redirect('appointment_success')
    else:
        form = AppointmentForm()
    return render(request, 'book_appointment.html', {'form': form, 'doctor': doctor})

def register_patient(request):
    if request.method == 'POST':
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = PatientRegistrationForm()
    return render(request, 'register.html', {'form': form})

def patient_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')

@login_required
def patient_logout(request):
    logout(request)
    return redirect('home')

def appointment_success(request):
    return render(request, 'appointment_success.html')
