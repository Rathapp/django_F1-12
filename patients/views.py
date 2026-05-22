from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse
from .models import patients,doctors

# Create your views here.
def home(request):
    return render(request,'patients/home.html')


def about(request):
    return render(request,'patients/about.html')

def register(request):
    patient = patients.objects.filter(Q(DateOfBirth__gt='2024-04-01') | Q(Sex='fenale'))
  
    return render(request,'patients/register.html',{'patients':patient})