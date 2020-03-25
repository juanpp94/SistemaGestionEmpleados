from django.conf.urls import url
from apps.vacaciones.views import solicitar,mostrar,iniciar
app_name = 'vacaciones'
urlpatterns=[
    url(r'^solicitar/$',solicitar,name='solicitar'),
    url(r'^mostrar/$',mostrar,name='mostrar'),
    url(r'^iniciar/(?P<pk>\d+)$',iniciar, name = 'iniciar'),
]