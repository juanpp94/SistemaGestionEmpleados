from django.conf.urls import url
from app import views
app_name = 'app'
urlpatterns=[
    url(r'^registro/$',views.registro,name='registro'),
    url(r'^ingreso/$',views.ingreso_usuario,name='ingreso'),
    url(r'^tarea/$',views.agregar_tarea,name='tarea'),
    url(r'^tiempo/$',views.tiempo_tarea,name='tiempo'),
]