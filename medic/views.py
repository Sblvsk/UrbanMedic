from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Doctor, Exercise, Patient
from .serializers import DoctorSerializer, ExerciseScheduledSerializer, ExerciseSerializer, PatientSerializer


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

    @action(detail=False, methods=["get"])
    def exercises_by_doctor(self, request):
        doctor_id = request.query_params.get("doctor_id")
        if doctor_id is not None:
            try:
                doctor = Doctor.objects.get(pk=doctor_id)
                exercises = doctor.exercise_doctors.all()
                serializer = ExerciseSerializer(exercises, many=True)
                return Response(serializer.data)
            except Doctor.DoesNotExist:
                return Response({"error": "Doctor not found."}, status=404)
        else:
            return Response({"error": "Doctor ID not provided."}, status=400)

    @action(detail=False, methods=["get"])
    def exercises_by_patient(self, request):
        patient_id = request.query_params.get("patient_id")
        if patient_id is not None:
            try:
                patient = Patient.objects.get(pk=patient_id)
                exercises = patient.exercises_assigned.all()
                serializer = ExerciseSerializer(exercises, many=True)
                return Response(serializer.data)
            except Patient.DoesNotExist:
                return Response({"error": "Patient not found."}, status=404)
        else:
            return Response({"error": "Patient ID not provided."}, status=400)

    @action(detail=False, methods=["get"])
    def exercises_scheduled(self, request):
        exercises = Exercise.objects.all()
        serializer = ExerciseScheduledSerializer(exercises, many=True)
        return Response(serializer.data)
