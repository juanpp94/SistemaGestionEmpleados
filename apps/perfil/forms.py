from django import forms
from app.models import InformacionUsuario

DOCUMENTOS = (
    ("V","V"),
    ("E","E")
)

SEXO = (
    ("M","M"),
    ("F","F"),
    ("O","O")
)

class PerfilForm(forms.ModelForm):
    nombre = forms.CharField(widget=forms.TextInput(attrs = { 'class': 'form-control'} ))
    apellido = forms.CharField(widget=forms.TextInput(attrs = { 'class': 'form-control'} ))
    foto_de_perfil = forms.ImageField(required=False, widget=forms.FileInput(attrs = { 'class': 'form-control-file'}))
    email_alternativo = forms.EmailField(required=False, widget=forms.EmailInput(attrs = { 'class': 'form-control'} ))
    tipo_documento = forms.ChoiceField(required=False, choices=DOCUMENTOS, widget=forms.Select(attrs = { 'class': 'form-control'} ))
    cedula = forms.IntegerField(required=False, widget=forms.NumberInput(attrs = { 'class' : 'form-control'}))
    edad = forms.DecimalField(required=False, widget=forms.NumberInput(attrs = { 'class' : 'form-control'}))
    sexo = forms.ChoiceField(required=False,choices=SEXO, widget=forms.Select(attrs = { 'class': 'form-control'} ))
    celular = forms.IntegerField(required=False, widget=forms.NumberInput(attrs = { 'class' : 'form-control'}))
    telefono = forms.IntegerField(required=False, widget=forms.NumberInput(attrs = { 'class' : 'form-control'}))
    domicilio = forms.CharField(required=False, widget=forms.TextInput(attrs = { 'class': 'form-control'} ))
    fecha_nacimiento = forms.DateField(required=False, widget=forms.DateInput(attrs = { 'class': 'form-control'}))
    class Meta():
        model = InformacionUsuario
        fields = ('nombre','apellido','email_alternativo','tipo_documento', 'cedula', 'edad', 'sexo', 'celular', 'telefono', 'domicilio', 'fecha_nacimiento','foto_de_perfil')