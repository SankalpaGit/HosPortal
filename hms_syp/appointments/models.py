from django.db import models
from django.contrib.auth.models import User

class Doctor(models.Model):
    name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)
    available_from = models.TimeField()
    available_to = models.TimeField()

    def __str__(self):
        return self.name

class Appointment(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    is_approved = models.BooleanField(default=True)  # Auto-approved when booked

    def __str__(self):
        return f"{self.patient.username} - {self.doctor.name} on {self.date}"

class AppointmentEditRequest(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE)
    new_date = models.DateField()
    new_time = models.TimeField()
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Edit Request for {self.appointment}"
