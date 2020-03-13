from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.index,name='index'),
    url(r'^app/',include('app.urls')),
    url(r'^salir/$', views.salir, name='salir'),
    url(r'^usuario/',include('apps.perfil.urls')),
    url(r'^tarea/',include('apps.tareas.urls')),
]