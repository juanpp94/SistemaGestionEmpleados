from django import forms
from apps.incidencias.models import Incidencia

TIPOS = (
    ("Retraso","Retraso"),
    ("Error","Error"),
    ("Ausencia","Ausencia"),
    ("Problema Tecnico","Problema Tecnico"),
    ("Otro","Otro"),
)

class IncidenciaForm(forms.ModelForm):
    titulo = forms.CharField(widget=forms.TextInput(attrs = { 'class': 'form-control'} ))
    descripcion = forms.CharField(widget=forms.Textarea(attrs = { 'class': 'form-control'} ))
    tipo = forms.ChoiceField(choices=TIPOS, widget=forms.Select(attrs = { 'class': 'form-control'} ))
    fecha_reportada = forms.DateField(widget=forms.DateInput(attrs = { 'class': 'form-control'}))
    class Meta():
        model = Incidencia
        fields = ('titulo','descripcion','tipo','fecha_reportada')