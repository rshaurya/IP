from django.urls import path

from users.views import AdmitPatient

urlpatterns = [

    path("admit-patient/", AdmitPatient.as_view()),


]