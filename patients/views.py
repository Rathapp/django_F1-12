from django.shortcuts import render,redirect,get_object_or_404
from django.db.models import Q
from django.http import HttpResponse
from .models import patients,doctors
from .form import PatientFormModel

# Create your views here.
def home(request):
    return render(request,'patients/home.html')


def about(request):
    return render(request,'patients/about.html')

def register(request,id=None):
    patient = patients.objects.all()

    pform = None
    if id:
        pform = get_object_or_404(patients,id=id)

    
    if request.method =="POST":

        form =PatientFormModel(request.POST,request.FILES,instance=pform)
        if form.is_valid():
            form.save()
            return redirect('register')
    else:
        form =PatientFormModel(instance= pform)
  
    return render(request,'patients/register.html',{'patients':patient,'patientform':form})

def delete(request,id):
    pat = get_object_or_404(patients,id=id)
    pat.delete()
    return redirect('register')
