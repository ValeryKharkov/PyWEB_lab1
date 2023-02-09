from django.shortcuts import render
from django.views import View


class IndexShopView(View):
   def get(self, request):
       return render(request, 'home/index.html')

class IndexAbout(View):
   def get(self, request):
       return render(request, 'home/about.html')

class IndexContact(View):
   def get(self, request):
       return render(request, 'home/contact.html')
