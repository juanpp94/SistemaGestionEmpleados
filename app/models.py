from django.db import models
from django.contrib.auth.models import User


Roles = (
	("Estudiante","Estudiante"),
	("Trainee","Trainee"),
	("Junior","Junior"),
	("Semi-junior","Semi-junior"),
	("Senior","Senior"),
)

class InformacionUsuario(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	cargo=models.CharField(max_length=40,choices=Roles, default="Estudiante")
	nombre = models.CharField(max_length=40, blank = True)
	apellido = models.CharField(max_length=40, blank = True)
	foto_de_perfil = models.ImageField(upload_to='foto_de_perfil',blank=True)
	
