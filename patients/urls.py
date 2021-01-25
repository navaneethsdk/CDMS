from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('patients/view_patients', views.view_patients, name='view-patient'),
    path('patients/view_wards', views.view_wards, name='view-wards'),
    path('patients/view_medicines', views.view_medicines, name='view-medicines'),
    path('patients/add_patient', views.add_patient, name='add-patient'),
    path('patients/add_guardian', views.add_guardian, name='add-guardian'),
]