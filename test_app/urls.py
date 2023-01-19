from django.urls import path
from .views import RandomNumber

urlpatterns = [
    path('random_number/', RandomNumber.as_view()),
]
