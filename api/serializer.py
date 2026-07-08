from rest_framework import serializers
from patients.models import patients

class Patientserializer(serializers.ModelSerializer):
    class Meta:
        model = patients
        fields = '__all__'