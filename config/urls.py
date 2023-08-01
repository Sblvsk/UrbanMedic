from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from medic.views import DoctorViewSet, PatientViewSet, ExerciseViewSet

router = DefaultRouter()

router.register(r'doctors', DoctorViewSet)
router.register(r'patients', PatientViewSet)
router.register(r'exercises', ExerciseViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path('exercises_by_doctor/', ExerciseViewSet.as_view({'get': 'exercises_by_doctor'}), name='exercises-by-doctor'),
    path('exercises_by_patient/', ExerciseViewSet.as_view({'get': 'exercises_by_patient'}), name='exercises-by-patient'),
    path('exercises_scheduled/', ExerciseViewSet.as_view({'get': 'exercises_scheduled'}), name='exercises-scheduled'),
]