from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
# from rest_framework import routers, serilizers, viewsets
from api.views import CustomAuthToken, JuegosList

urlpatterns = [
    re_path('login', CustomAuthToken.as_view()),
    re_path('juegos',JuegosList.as_view()),
]