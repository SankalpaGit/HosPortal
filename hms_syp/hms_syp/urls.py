from django.urls import path
from django.contrib import admin
from appointments import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('doctors/', views.doctor_list, name='doctor_list'),
    path('book-appointment/<int:doctor_id>/', views.book_appointment, name='book_appointment'),
    path('register/', views.register_patient, name='register'),
    path('login/', views.patient_login, name='login'),
    path('logout/', views.patient_logout, name='logout'),
    path('appointment-success/', views.appointment_success, name='appointment_success'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
