from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from patients.models import patients
from .serializer import PatientSerializer
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .pagination import StandardPagination
from .filter import PatientFilter
from rest_framework.filters import SearchFilter,OrderingFilter
# Create your views here.
class PatientList(ListCreateAPIView):
    queryset = patients.objects.all()
    serializer_class = PatientSerializer
    permission_classes= [IsAuthenticated]
    pagination_class=StandardPagination
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]

    # filterset_fields = [
    #  'firstName',
            # 'lastName',
            # 'Sex',
            # 'Phone' 
       
    # ]
    filterset_class =PatientFilter
    search_fields = [
     'firstName',
        'lastName',
        'Sex',
        'Phone' 
]
    ordering_fields = [
    
    'created',
     'firstName',
        'lastName',
        'Sex',
        'Phone' 
    
]




class PatientDetal(RetrieveUpdateDestroyAPIView):
    queryset = patients.objects.all()
    serializer_class = PatientSerializer
    permission_classes= [IsAuthenticated]
