from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('doctor/view_doctor', views.view_doctor, name='view-doctor'),
]