from django.db import models
from django.contrib.auth.models import User
# Create your models here.

STATUS = (
    ("Pendiente","Pendiente"),
    ("Aprobada","Aprobada"),
    ("Activa","Activa"),
    ("Rechazada","Rechazada"),
)

class Vacaciones(models.Model):
    nro_dias = models.IntegerField()
    fecha_inicio = models.DateTimeField(null = True)
    status = models.CharField(max_length=20,choices=STATUS, default="Pendiente")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
