from django import forms
from apps.vacaciones.models import Vacaciones

class VacacionesForm(forms.ModelForm):

    class Meta:
        model = Vacaciones
        fields = [
            'nro_dias',
            
        ]
        labels = {
            'nro_dias' : 'Cantidad de días',
            
        }
        widgets = {
            'nro_dias' : forms.TextInput(attrs={'class':'form-control'}),
        }
    def clean_nro_dias(self): 
        data = self.cleaned_data['nro_dias']
        if data > 19:
            raise forms.ValidationError("Numero de dias invalidos")

        return data   