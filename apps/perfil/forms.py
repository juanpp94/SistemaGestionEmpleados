from django import forms
from app.models import InformacionUsuario

class PerfilForm(forms.ModelForm):
    nombre = forms.CharField(widget=forms.TextInput(attrs = { 'class': 'form-control'} ))
    apellido = forms.CharField(widget=forms.TextInput(attrs = { 'class': 'form-control'} ))
    foto_de_perfil = forms.ImageField(required=False, widget=forms.FileInput(attrs = { 'class': 'form-control-file'}))
    class Meta():
        model = InformacionUsuario
        fields = ('nombre','apellido','foto_de_perfil')