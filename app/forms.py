from django import forms
from app.models import InformacionUsuario, Tarea
from django.contrib.auth.models import User

class Formulario_Usuario(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')

class Formulario_Datos_Perfil(forms.ModelForm):
	class Meta():
		model = InformacionUsuario
		fields = ('nombre','apellido','foto_de_perfil')

class Formulario_Tarea(forms.ModelForm):
	class Meta():
		model = Tarea
		fields = ('nombre_tarea',)