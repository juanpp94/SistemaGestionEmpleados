from django.contrib import admin
from apps.tareas.models import Tarea

class TareaAdmin(admin.ModelAdmin):
    # ...
    list_display = ('usuario', 'nombre_tarea', 'status')

admin.site.register(Tarea, TareaAdmin)