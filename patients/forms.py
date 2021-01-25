from django import forms
from .models import Patient, Ward, Guardian

class PatientForm(forms.ModelForm):
    patient_id = forms.IntegerField(widget=forms.HiddenInput(), initial=Patient.objects.count()+1)
    first_name = forms.CharField(max_length=30, help_text="Enter the First name")
    last_name = forms.CharField(max_length=30, help_text="Enter the Last name")
    birthday = forms.DateField(help_text="Enter the Date of Birth")
    gender = forms.CharField(max_length=100, help_text="Enter the Male/Female")
    street_address = forms.CharField(max_length=100, help_text="Enter the Street Address")
    district = forms.CharField(max_length=100, help_text="Enter the District")
    zip_code = forms.CharField( max_length=6, help_text="Enter the Pincode")
    p_level = forms.IntegerField(help_text="Enter the Progress level",initial=1)
    w_id = forms.ModelChoiceField(queryset=Ward.objects.all(), help_text="Enter the ward id")

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Patient
        fields = ('patient_id', 'first_name', 'last_name', 'birthday', 'gender', 'street_address', 'district', 'zip_code', 'p_level', 'w_id')

class GuardianForm(forms.ModelForm):
    patient_id = forms.ModelChoiceField(queryset=Patient.objects.all(), help_text="Enter the ward id")
    first_name = forms.CharField(max_length=128, help_text="Enter the First name")
    last_name = forms.CharField(max_length=128, help_text="Enter the Last name")
    address = forms.CharField(max_length=128, help_text="Enter the Address")
    relationship = forms.CharField(max_length=128, help_text="Enter the Relation")
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Guardian
        fields = ('patient_id', 'first_name', 'last_name', 'address', 'relationship')