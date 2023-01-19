from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from datetime import datetime


# Create your views here.
class CurrentDateView(View):
    def get(self, request):
        html = f'{datetime.now()}'
        return HttpResponse(html)
