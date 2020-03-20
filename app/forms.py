from django import forms
from app.models import InformacionUsuario
from django.contrib.auth.models import User

class Formulario_Usuario(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField()
    class Meta():
        model = User
        fields = ('username','password','email')

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        if not email.endswith('@ubicutus.com'):
            raise forms.ValidationError("No es un correo @ubicutus.com")
        return email

class Formulario_Datos_Perfil(forms.ModelForm):
	class Meta():
		model = InformacionUsuario
		fields = ('cargo','nombre','apellido','foto_de_perfil')