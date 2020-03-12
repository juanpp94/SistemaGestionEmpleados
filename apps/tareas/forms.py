from django import forms
from apps.tareas.models import Tarea

class TareaForm(forms.ModelForm):

    class Meta:
        model = Tarea
        fields = [
            'nombre_tarea',
            
        ]
        labelds = {
            'nombre_tarea' : 'Nombre',
            
        }
        widgets = {
            'nombre_tarea' : forms.TextInput(attrs={'class':'form-control'}),
        }