from django import forms
from apps.vacaciones.models import Vacaciones

class VacacionesForm(forms.ModelForm):

    class Meta:
        model = Vacaciones
        fields = [
            'nro_dias',
            
        ]
        labelds = {
            'nro_dias' : 'Cantidad de dias',
            
        }
        widgets = {
            'nro_dias' : forms.TextInput(attrs={'class':'form-control'}),
        }