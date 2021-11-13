from django.shortcuts import render
from django.views.generic import View
from .models import UserData
from .utils import *




class VaccinePageView(View):
    def get(self, request, pk):
        user = UserData.objects.get(id=pk)
        content = vaccine_structure(user)
        return render(request, 'vaccinePage.html', content)
