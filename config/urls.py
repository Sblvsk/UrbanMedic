"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from medic.views import DoctorViewSet, PatientViewSet, ExerciseViewSet, DoctorExerciseListView, PatientExerciseListView

router = DefaultRouter()

router.register('doctors', DoctorViewSet)
router.register('patients', PatientViewSet)
router.register('exercises', ExerciseViewSet)
router.register('doctors/<int:doctor_id>/exercises', DoctorExerciseListView, basename='doctor-exercises')
router.register('patients/<int:patient_id>/exercises', PatientExerciseListView, basename='patient-exercises')

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include(router.urls)),
]
