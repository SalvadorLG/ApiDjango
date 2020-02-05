from django.urls import re_path
from api.views import CustomAuthToken

from api.viewsets import JuegosViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register('juegos',JuegosViewSet)

urlpatterns = [
    re_path('login', CustomAuthToken.as_view()),
    #re_path('juegos',JuegosList.as_view()),
]

urlpatterns += router.urls
