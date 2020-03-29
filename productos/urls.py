from django.urls import re_path, path
#from .views import CustomAuthToken, RegisterUser
from rest_framework.routers import DefaultRouter

from productos.views import Registrar, UsuariosList
#UserListCreateView, userDetailView
#from api.viewsets import JuegosViewSet
#from rest_framework import routers

#router = routers.SimpleRouter()
#router.register('juegos',JuegosViewSet)

urlpatterns = [
    #re_path('register', RegisterUser.as_view()),
    #gets all user profiles and create a new profile
    #path('all-profiles/', UserListCreateView.as_view(),name='allprofiles'),
   # retrieves profile details of the currently logged in user
    #path('profile/<int:pk>',userDetailView.as_view(),name='profile'),
    #re_path('login', CustomAuthToken.as_view()),
    #re_path('juegos',JuegosList.as_view()),
    re_path(r'^perfil/$', UsuariosList.as_view() ),
    re_path(r'^perfil/registrar/$', Registrar.as_view() ),
    re_path(r'^perfil/(?P<id>\d+)$', Registrar.as_view() ),
]

#urlpatterns += router.urls