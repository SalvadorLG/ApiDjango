from django.db import models

# Create your models here.
class Juegos(models.Model):
    nombre = models.CharField(max_length=200)
    genero = models.CharField(max_length=150)
    