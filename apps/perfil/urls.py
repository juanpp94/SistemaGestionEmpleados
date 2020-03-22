from django.conf.urls import url
from apps.perfil.views import perfil_list,perfil_edit
app_name = 'perfil'
urlpatterns=[
    url(r'^perfil/$',perfil_list,name='perfil_list'),
    url(r'^perfil/modificar$',perfil_edit,name='perfil_edit'),
]