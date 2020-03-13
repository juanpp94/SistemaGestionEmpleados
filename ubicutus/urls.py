from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.ingreso_usuario,name='ingreso'),
    url(r'^registro',views.registro,name='registro'),
    url(r'^index1/',views.index1,name='index1'),
    url(r'^index/',views.index,name='index'),
    url(r'^app/',include('app.urls')),
    url(r'^salir/$', views.salir, name='salir'),
    url(r'^usuario/',include('apps.perfil.urls')),
    url(r'^tarea/',include('apps.tareas.urls')),
]