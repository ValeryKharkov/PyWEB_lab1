from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from datetime import datetime


# Create your views here.
class CurrentDateView(View):
    def get(self, request):
        html = f'{datetime.now()}'
        return HttpResponse(html)


class Greeting(View):
    def get(self, request):
        greeting = '<h1>Hello, World</h1>'
        return HttpResponse(greeting)


class IndexView(View):
   def get(self, request):
       return render(request, 'common/index.html')