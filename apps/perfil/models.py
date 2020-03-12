from django.db import models
from app.models import InformacionUsuario

class Perfil(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=70)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=12)
    email = models.EmailField()
    domicilio = models.TextField()
    usuario = models.ForeignKey(InformacionUsuario, on_delete=models.CASCADE)

