from django.contrib import admin
from apps.incidencias.models import Incidencia

class IncidenciaAdmin(admin.ModelAdmin):
    # ...
    list_display = ('usuario', 'titulo', 'estatus', 'tipo', 'fecha_reportada', 'fecha_reporte')

admin.site.register(Incidencia, IncidenciaAdmin)