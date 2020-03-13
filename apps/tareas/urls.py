from django.conf.urls import url
from apps.tareas.views import agregar_tarea,tiempo_tarea,listar_tarea,iniciar_tarea,finalizar_tarea
app_name = 'tarea'
urlpatterns=[
    url(r'^agregar/$',agregar_tarea,name='agregar_tarea'),
    url(r'^listar/',listar_tarea, name = 'listar_tareas'),
    url(r'^tiempo/(?P<pk>\d+)$',tiempo_tarea, name = 'tiempo'),
    url(r'^iniciar/(?P<pk>\d+)$',iniciar_tarea, name = 'iniciar'),
    url(r'^finalizar/(?P<pk>\d+)$',finalizar_tarea, name = 'finalizar'),
]