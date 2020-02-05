from rest_framework import serializers
from .models import Juegos

class JuegosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Juegos
        fields = '__all__'