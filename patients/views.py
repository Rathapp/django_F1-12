from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'patients/home.html')


def about(request):
    return render(request,'patients/about.html')

def register(request):
    return render(request,'patients/register.html')

