from django.urls import path
from .views import IndexShopView, IndexAbout, IndexContact

app_name = 'home'

urlpatterns = [
   path('', IndexShopView.as_view(), name='index'),
   path('', IndexAbout.as_view(), name='about'),
   path('', IndexContact.as_view(), name='contact'),

]

