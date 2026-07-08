from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from .views import PatientList,PatientDetal

urlpatterns = [
    path('login/',TokenObtainPairView.as_view(),name='login'),
    path('refresh/',TokenRefreshView.as_view(),name='refresh'),
    path('patients/',PatientList.as_view(),name='patient_list'),
    path('patients/<int:pk>/',PatientDetal.as_view(),name='patient_list')
    
]
