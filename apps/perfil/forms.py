from django import forms
from app.models import InformacionUsuario

class PerfilForm(forms.ModelForm):

    class Meta:
        model = InformacionUsuario
        fields = [
            'nombre',
            'apellido',
        ]
        labelds = {
            'nombre' : 'Nombre',
            'sexo' : 'Apellido',
        }
        widgets = {
            'nombre' : forms.TextInput(attrs={'class':'form-control'}),
            'apellido' : forms.TextInput(attrs={'class':'form-control'}),
        }