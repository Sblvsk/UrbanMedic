from django.db import models


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=50)

    def str(self):
        return self.name


class Patient(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def str(self):
        return f"{self.first_name} {self.last_name}"


class Exercise(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    periodicity = models.PositiveIntegerField()
    doctors = models.ManyToManyField(Doctor, related_name="exercise_doctors")
    patients = models.ManyToManyField(Patient, related_name="exercises_assigned")

    class Meta:
        ordering = ['title']
