from django.urls import path
from .views import ViewBlog

app_name = 'blog'

urlpatterns = [
   path('', ViewBlog.as_view(), name='blog'),
]

