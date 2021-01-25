from django.db import models

class Department(models.Model):
    d_name = models.CharField(max_length=100, primary_key=True)
    d_number = models.IntegerField(blank=False, unique=True)

    def __str__(self): 
        return self.d_name

class Doctor(models.Model):
    doctor_id = models.IntegerField(default=1,primary_key=True)
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30)
    birthday = models.DateField(null=True, blank=True)
    d_name = models.ForeignKey(Department, on_delete=models.CASCADE)
    gender = models.CharField(max_length=100)
    exp = models.CharField(max_length=100)
    sup_id = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subdoctors')
    
    def __str__(self): 
        return self.first_name


