from django.urls import path
from .views import patient_list,patientDetail

urlpatterns = [
    
    path('patients/',patient_list,name='patient_list'),
    path('patients/<int:pk>/',patientDetail,name='patient_detail')
]
