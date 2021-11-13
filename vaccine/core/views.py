from django.shortcuts import render
from django.views.generic import View
from .models import UserData
from .utils import *


class VaccinePageView(View):
    @staticmethod
    def get(request, pk):
        user = UserData.objects.get(id=pk)
        content = vaccine_structure(user)
        print(content)
        return render(request, 'vaccinePage.html', content)
