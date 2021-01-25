from django.shortcuts import render, redirect
from .forms import PatientForm, GuardianForm
from .models import Patient, Medicine, Ward


def home(request):
    return render(request, 'patients/home.html')

def view_patients(request):
    context = {
        'Patients': Patient.objects.all()
    }
    return render(request, 'patients/view_patients.html', context)

def view_wards(request):
    context = {
        'Wards': Ward.objects.all()
    }
    return render(request, 'patients/view_wards.html', context)

def view_medicines(request):
    context = {
        'Medicines': Medicine.objects.all()
    }
    return render(request, 'patients/view_medicines.html', context)

def add_patient(request):

    # A HTTP POST?
    if request.method == 'POST':
        form = PatientForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return redirect('add-guardian')
        else:
            # The supplied form contained errors - just print them to the terminal.
            print(form.errors)
    else:
        # If the request was not a POST, display the form to enter details.
        form = PatientForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request,'patients/add_patients.html', {'form': form})


def add_guardian(request):

    # A HTTP POST?
    if request.method == 'POST':
        form = GuardianForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return redirect('home')
        else:
            # The supplied form contained errors - just print them to the terminal.
            print(form.errors)
    else:
        # If the request was not a POST, display the form to enter details.
        form = GuardianForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request,'patients/add_guardians.html', {'form': form})