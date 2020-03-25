from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Vacaciones(models.Model):
    nro_dias = models.IntegerField()
    fecha_inicio = models.DateTimeField(null = True)
    status = models.CharField(max_length=20)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
