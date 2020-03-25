from django import forms
from apps.tareas.models import Tarea

class TareaForm(forms.ModelForm):

    class Meta:
        model = Tarea
        fields = [
            'nombre_tarea',
            'descripcion'
            
        ]
        labelds = {
            'nombre_tarea' : 'Nombre',
            'descripcion' : 'Descripcion'
        }
        widgets = {
            'nombre_tarea' : forms.TextInput(attrs={'class':'form-control'}),
            'descripcion' : forms.Textarea(attrs={'class':'form-control'})
        }