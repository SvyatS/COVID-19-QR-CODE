from django.urls import path

from .views import VaccinePageView, VaccineQrCodeView

urlpatterns = [
    path('covid-cert/status/<slug:pk>', VaccinePageView.as_view()),
    path('covid-cert/qr-code/<slug:pk>', VaccineQrCodeView.as_view()),
]
