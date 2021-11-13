from django.urls import path

from .views import VaccinePageView




urlpatterns = [
    path('covid-cert/status/<slug:pk>', VaccinePageView.as_view()),
]