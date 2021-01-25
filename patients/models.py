from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from doctor.models import Doctor
 

class Ward(models.Model):
    w_id = models.IntegerField(default=1, blank=False, primary_key=True)
    ward_id = models.IntegerField(default=1, validators=[MaxValueValidator(100), MinValueValidator(1)],blank=False)
    d_stage = models.IntegerField(default=1, validators=[MaxValueValidator(5), MinValueValidator(1)],blank=False)
    doctor_id = models.ManyToManyField(Doctor)

    def __str__(self):
        return str(self.w_id)


class Patient(models.Model):
    patient_id = models.IntegerField(default=1,primary_key=True)
    # guardian_id = models.OneToOneField(Guardian, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30)
    birthday = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=100, default='Male')
    street_address = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    zip_code = models.CharField( max_length=6, default="43701", blank=False)
    p_level = models.IntegerField(default=1, validators=[MaxValueValidator(10), MinValueValidator(1)],blank=False)
    w_id = models.ForeignKey(
        Ward,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.first_name

class Guardian(models.Model):
    patient_id = models.OneToOneField(Patient, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, primary_key=True,blank=False)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    relationship = models.CharField(max_length=100)
    
    class Meta:
        unique_together = (("patient_id", "first_name"),)

    def __str__(self):
        return self.first_name


class Medicine(models.Model):
    name = models.CharField(max_length=30)
    quantity = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    patient_id = models.ManyToManyField(Patient)


    def __str__(self):
        return self.name