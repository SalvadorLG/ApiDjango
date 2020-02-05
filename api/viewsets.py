from rest_framework import viewsets
from api.models import Juegos
from api.serializers import JuegosSerializer

class JuegosViewSet(viewsets.ModelViewSet):
    queryset = Juegos.objects.all()
    serializer_class = JuegosSerializer