from django import forms
from apps.tareas.models import Tarea

class TareaForm(forms.ModelForm):

    class Meta:
        model = Tarea
        fields = [
            'nombre_tarea',
            'descripcion'
            
        ]
        labels = {
            'nombre_tarea' : 'Nombre',
            'descripcion' : 'Descripción'
        }
        widgets = {
            'nombre_tarea' : forms.TextInput(attrs={'class':'form-control'}),
            'descripcion' : forms.Textarea(attrs={'class':'form-control'})
        }