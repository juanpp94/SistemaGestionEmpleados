from django.contrib import admin
from app.models import InformacionUsuario, User

class InformacionUsuarioAdmin(admin.ModelAdmin):
    # ...
    list_display = ('user', 'nombre', 'apellido', 'cargo', 'edad', 'sexo', 'celular')

admin.site.register(InformacionUsuario, InformacionUsuarioAdmin)