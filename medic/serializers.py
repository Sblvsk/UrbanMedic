from datetime import date, timedelta

from rest_framework import serializers

from .models import Doctor, Exercise, Patient


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = "__all__"


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = "__all__"


class ExerciseScheduledSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ("id", "title", "description", "periodicity")

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        periodicity = representation["periodicity"]
        today = date.today()
        next_scheduled_date = today + timedelta(days=periodicity)
        representation["next_scheduled_date"] = next_scheduled_date.strftime("%Y-%m-%d")
        return representation
