from django.contrib import admin
from .models import Patient, Ward, Medicine, Guardian

admin.site.register(Patient)
admin.site.register(Ward)
admin.site.register(Guardian)
admin.site.register(Medicine)
