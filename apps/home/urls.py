from django.urls import path
from .views import IndexShopView

app_name = 'home'

urlpatterns = [
   path('', IndexShopView.as_view(), name='index'),
]

