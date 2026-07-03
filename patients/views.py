from django.shortcuts import render,redirect,get_object_or_404
from django.db.models import Q
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.http import HttpResponse
from .models import patients,doctors
from .form import PatientFormModel

# Create your views here.
@login_required
def home(request):
    return render(request,'patients/home.html')

def userLogin(request):

    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"Log in sucessful")
            return redirect("home")
        else:
            messages.error(request,"Username Or Password is Invalid")
            return render(request,'patients/login.html')

    return render(request,'patients/login.html')

def userLogout(request):
    logout(request)
    return redirect("login")

@login_required
def about(request):
    return render(request,'patients/about.html')
@login_required
def register(request,id=None):
    patient = patients.objects.all()

    pform = None
    if id:
        pform = get_object_or_404(patients,id=id)
    
    if request.method =="POST":

        form =PatientFormModel(request.POST,request.FILES,instance=pform)
        if form.is_valid():
            form.save()
            messages.success(request,"Save data sucessful")
            return redirect('register')
    else:
        form =PatientFormModel(instance= pform)
  
    return render(request,'patients/register.html',{'patients':patient,'patientform':form})
@login_required
def delete(request,id):
    pat = get_object_or_404(patients,id=id)
    pat.delete()
    messages.info(request,"Delete Sucessful")
    return redirect('register')
