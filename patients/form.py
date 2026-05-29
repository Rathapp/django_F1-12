from django import forms
from .models import patients

class PatientFormModel(forms.ModelForm):
    class Meta:
        model = patients
        fields = '__all__'

        widgets={
            'firstName':forms.TextInput(attrs={ 'class':'form-control'}),
            'DateOfBirth': forms.DateInput(attrs={ 'class':'form-control','type':'date'}),
            'Sex':forms.Select(attrs={ 'class':'form-control'}),
            'picture': forms.FileInput(attrs={ 'class':'form-control'}),
            
        }
