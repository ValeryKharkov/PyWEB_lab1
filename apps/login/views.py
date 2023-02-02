from django.shortcuts import render
from django.http import JsonResponse
from django.views import View


# Create your views here.

class IndexView(View):
    def get(self, request):
        return render(request, 'login/index.html')

    def post(self, request):
        print("post")
        return JsonResponse(request.POST, json_dumps_params={'indent': 4})


class LoginView(View):
    def get(self, request):
        print("get")
        return render(request, 'login/index.html')

