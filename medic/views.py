from rest_framework import viewsets

from .models import Doctor, Exercise, Patient
from .serializers import DoctorSerializer, ExerciseSerializer, PatientSerializer, DoctorExerciseSerializer, \
    PatientExerciseSerializer


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer


class DoctorExerciseListView(viewsets.ReadOnlyModelViewSet):
    serializer_class = DoctorExerciseSerializer

    def get_queryset(self):
        doctor_id = self.kwargs['doctor_id']
        return Exercise.objects.filter(doctors__id=doctor_id)


class PatientExerciseListView(viewsets.ReadOnlyModelViewSet):
    serializer_class = PatientExerciseSerializer

    def get_queryset(self):
        patient_id = self.kwargs['patient_id']
        return Exercise.objects.filter(patients__id=patient_id)
