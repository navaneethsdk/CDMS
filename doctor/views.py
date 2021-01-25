from django.shortcuts import render
from .models import Doctor

def view_doctor(request):
    context = {
        'Doctors': Doctor.objects.all()
    }
    return render(request, 'doctor/view_doctors.html', context)
