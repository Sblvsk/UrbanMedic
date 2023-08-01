from rest_framework import serializers

from .models import Doctor, Exercise, Patient


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = "all"


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = "all"


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = "all"
