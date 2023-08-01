from django.contrib import admin

from .models import Doctor, Exercise, Patient

admin.site.register([Doctor, Patient, Exercise])
