from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseNotFound
from .models import UserData
from .utils import *


class VaccinePageView(View):
    @staticmethod
    def get(request, pk):
        try:
            user = UserData.objects.get(id=pk)
            content = vaccine_structure(user)
            return render(request, 'vaccinePage.html', content)
        except Exception as e:
            return HttpResponseNotFound('<h1>User not found</h1>')


class VaccineQrCodeView(View):
    @staticmethod
    def get(request, pk):
        try:
            print(request.get_host() + "/covid-cert/status/" + str(pk))
            url = request.get_host() + "/covid-cert/status/" + str(pk)
            return render(request, 'vaccineQR.html', {"url": url})
        except Exception as e:
            return HttpResponseNotFound('<h1>User not found</h1>')