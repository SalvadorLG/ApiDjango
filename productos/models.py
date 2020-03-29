from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    perfil = models.OneToOneField(User, on_delete=models.CASCADE)
    tipo = models.IntegerField(null = True)
    
    class Meta:
        db_table = 'usuario'

class Producto(models.Model):
    producto = models.CharField(max_length=150)
    precio = models.IntegerField(null = True)
    cantidadTotal = models.IntegerField(null = True)
    codigo = models.CharField(max_length=150)

    class Meta:
        db_table = 'producto'

class Detalles(models.Model):
    usuario = models.ForeignKey(Usuario, related_name='usuario_name', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, related_name='producto_name', on_delete=models.CASCADE)
    codigo = models.CharField(max_length=150)
    precio = models.IntegerField(null = True)
    cantidad = models.IntegerField(null = True)

    class Meta:
        db_table = 'detalles'