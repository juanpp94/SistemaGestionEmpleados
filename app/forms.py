from django import forms
from app.models import InformacionUsuario
from django.contrib.auth.models import User

class Formulario_Usuario(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')

class Formulario_Datos_Perfil(forms.ModelForm):
	class Meta():
		model = InformacionUsuario
		fields = ('cargo','nombre','apellido','foto_de_perfil')