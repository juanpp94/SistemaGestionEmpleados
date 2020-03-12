from django.db import models
from django.contrib.auth.models import User

class InformacionUsuario(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	nombre = models.CharField(max_length=40, blank = True)
	apellido = models.CharField(max_length=40, blank = True)
	foto_de_perfil = models.ImageField(upload_to='foto_de_perfil',blank=True)

class Tarea(models.Model):
	nombre_tarea = models.CharField(max_length=140)
	tiempo_inicio = models.DateTimeField(auto_now=False, auto_now_add=True)
	tiempo_fin = models.DateTimeField(auto_now=True, auto_now_add=False)
	
