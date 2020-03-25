from django import forms
from app.models import InformacionUsuario
from django.contrib.auth.models import User

class Formulario_Usuario(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs = { 'class': 'form-control'} ))
    password = forms.CharField(widget=forms.PasswordInput(attrs = { 'class': 'form-control'} ))
    email = forms.EmailField(widget=forms.EmailInput(attrs = { 'class': 'form-control'} ))
    class Meta():
        model = User
        fields = ('username','password','email')

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        if not email.endswith('@ubicutus.com'):
            raise forms.ValidationError("No es un correo @ubicutus.com")
        return email

Roles = (
	("Estudiante","Estudiante"),
	("Trainee","Trainee"),
	("Junior","Junior"),
	("Semi-junior","Semi-junior"),
	("Senior","Senior"),
)

class Formulario_Datos_Perfil(forms.ModelForm):
    cargo = forms.ChoiceField(choices=Roles, widget=forms.Select(attrs = { 'class': 'form-control'} ))
    nombre = forms.CharField(widget=forms.TextInput(attrs = { 'class': 'form-control'} ))
    apellido = forms.CharField(widget=forms.TextInput(attrs = { 'class': 'form-control'} ))
    foto_de_perfil = forms.ImageField(required=False, widget=forms.FileInput(attrs = { 'class': 'form-control-file'}))
    class Meta():
        model = InformacionUsuario
        fields = ('cargo','nombre','apellido','foto_de_perfil')