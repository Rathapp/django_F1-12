from django.contrib import admin
from .models import patients,doctors,appoinment

# Register your models here.
admin.site.register(patients)
admin.site.register(doctors)
admin.site.register(appoinment)
