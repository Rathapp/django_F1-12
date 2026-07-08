# from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from patients.models import patients
from .serializer import Patientserializer
# Create your views here.
@api_view(['GET','POST'])
def patient_list(request):

    if request.method == 'POST':
        serializer = Patientserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    else:
        patt = patients.objects.all()
        serializer = Patientserializer(patt,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
@api_view(['GET','PUT','DELETE'])  
def patientDetail(request,pk):

    try:
        ppp = patients.objects.get(id=pk)
    
    except patients.DoesNotExist:
        return Response({'message':'Patient not found'},status=status.HTTP_404_NOT_FOUND)
    
    if request.method =="GET":
        serializer = Patientserializer(ppp,many=False)
        return Response(serializer.data,status=status.HTTP_200_OK)
    if request.method =="PUT":
         serializer = Patientserializer(ppp,data=request.data)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data,status=status.HTTP_201_CREATED)
         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    if request.method =="DELETE":
        ppp.delete()
        return Response({'message':'Delete Sucessful!'},status=status.HTTP_200_OK)
    

