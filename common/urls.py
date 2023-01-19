from django.urls import path
from .views import CurrentDateView, Greeting, IndexView

urlpatterns = [
    path('datetime/', CurrentDateView.as_view()),
    path('greeting/', Greeting.as_view()),
    path('index/', IndexView.as_view())

]
