from django.db import models
from django.contrib.auth.models import User

ESTATUS = (
    ("Por Revisar","Por Revisar"),
    ("Revisado","Revisado"),
    ("Resuelto","Resuelto"),
    ("Descartada","Descartada"),
)

TIPOS = (
    ("Retraso","Retraso"),
    ("Error","Error"),
    ("Ausencia","Ausencia"),
    ("Problema Tecnico","Problema Tecnico"),
    ("Otro","Otro"),
)

class Incidencia(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=40, blank = True)
    estatus = models.CharField(max_length=40, choices=ESTATUS, default="Por Revisar")
    tipo = models.CharField(max_length=40, choices=TIPOS, default="Retraso")
    descripcion = models.CharField(max_length=200, blank = True)
    fecha_reporte = models.DateField(auto_now=False, auto_now_add=True)
    fecha_reportada = models.DateField(auto_now=False, auto_now_add=False)