from django.db import models
from django.contrib.auth.models import User


Roles = (
	("Estudiante","Estudiante"),
	("Trainee","Trainee"),
	("Junior","Junior"),
	("Semi-junior","Semi-junior"),
	("Senior","Senior"),
)

DOCUMENTOS = (
	("V","V"),
	("E","E")
)

SEXO = (
	("M","M"),
	("F","F"),
	("O","O")
)

class InformacionUsuario(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	cargo = models.CharField(max_length=40,choices=Roles, default="Estudiante")
	nombre = models.CharField(max_length=40, blank = True)
	apellido = models.CharField(max_length=40, blank = True)
	foto_de_perfil = models.ImageField(upload_to='foto_de_perfil',blank=True)
	email_alternativo = models.EmailField(blank=True, default="")
	tipo_documento = models.CharField(max_length=1,choices=DOCUMENTOS, blank=True, default="")
	cedula = models.PositiveIntegerField(blank=True, default=0)
	edad = models.DecimalField(max_digits=3, decimal_places=0,blank=True, default=0)
	sexo = models.CharField(max_length=1,choices=SEXO,blank=True, default="")
	celular = models.PositiveIntegerField(blank=True, default=0)
	telefono = models.PositiveIntegerField(blank=True, default=0)
	domicilio = models.CharField(max_length=200,blank=True, default="")
	fecha_nacimiento = models.DateField(auto_now=False, auto_now_add=False,blank=True, default="2020-03-26")
	fecha_ingreso = models.DateField(auto_now=False, auto_now_add=False,blank=True, default="2020-03-26")

	# podria ser un plus luego
	# idiomas = models # ?
	# habilidades = models # ? frontend, backend, full-stack, bd, etc
	# lenguajes = models # ? lenguajes de programacion
	# frameworks = models # ? frameworks