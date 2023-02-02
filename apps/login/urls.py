from django.urls import path
from .views import IndexView

urlpatterns = [
    path('login/', IndexView.as_view()),

]
