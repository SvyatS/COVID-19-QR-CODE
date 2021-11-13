from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseNotFound
import socket
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
            # request.get_host()
            url = "http://" + socket.gethostbyname(socket.gethostname()) + ":8000" + "/covid-cert/status/" + str(pk)
            print(socket.gethostbyname(socket.gethostname()))
            return render(request, 'vaccineQR.html', {"url": url})
        except Exception as e:
            return HttpResponseNotFound('<h1>QR code not found</h1>')