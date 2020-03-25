from django.conf.urls import url
from .views import incidencias_list_view, incidencia_crear, incidencia_mostrar, incidencia_editar, incidencia_descartar

app_name = 'incidencias'
urlpatterns=[
    url(r'^$',incidencias_list_view, name = 'lista'),
    url(r'^reportar',incidencia_crear, name = 'reportar'),
    url(r'^(?P<pk>\d+)$',incidencia_mostrar, name = 'mostrar'),
    url(r'^editar/(?P<pk>\d+)$',incidencia_editar, name = 'editar'),
    url(r'^eliminar/(?P<pk>\d+)$',incidencia_descartar, name = 'eliminar'),
]