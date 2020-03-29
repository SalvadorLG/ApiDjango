from rest_framework import serializers
from productos.models import Usuario, Producto, Detalles

class UsuariosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuario
        fields = '__all__'
"""
class DetallesSerializer(serializers.ModelSerializer):
    usuario_name = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='username'
        )

    producto_name = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='producto'
        )

    class Meta:
        model = Detalles
        fields = ('name','usuario_name','producto_name')

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

"""
