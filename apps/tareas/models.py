from django.db import models
from django.contrib.auth.models import User
# Create your models here.

CHOICES = (
    ('activa', 'Por Terminar'),
    ('finalizada', 'Finalizada'),
)

class Tarea(models.Model):
    nombre_tarea = models.CharField(max_length=140)
    tiempo_inicio = models.DateTimeField(auto_now=False, auto_now_add=True)
    tiempo_fin = models.DateTimeField(auto_now=True, auto_now_add=False)
    tiempo_total = models.FloatField(default=0.0)
    tiempo_total_formato = models.CharField(max_length=100, null=True)
    status = models.CharField("",max_length=10, null=True, choices=CHOICES)
    descripcion = models.TextField(max_length=200,null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
