from django.contrib import admin
from .models import Doctor, Appointment, AppointmentEditRequest, Patient
from django.contrib.auth.admin import UserAdmin


class PatientAdmin(UserAdmin):  # Extending Django's UserAdmin
    fieldsets = UserAdmin.fieldsets + (
        ("Additional Info", {"fields": ("phone", "address")}),
    )

admin.site.register(Patient, PatientAdmin)
admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(AppointmentEditRequest)
