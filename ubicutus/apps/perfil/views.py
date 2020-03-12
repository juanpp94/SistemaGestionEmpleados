from django.shortcuts import render,redirect
from app.models import InformacionUsuario
from django.contrib.auth.models import User
from django.template import RequestContext
from apps.perfil.forms import PerfilForm

# Create your views here.

def perfil_list(request):
    user= request.user.id
    perfil = InformacionUsuario.objects.get(user_id=user)
    contexto = {'perfil' : perfil}
    return render(request,'perfiles/perfiles_list.html',contexto)  
   

def perfil_edit(request, pk):
    perfil = InformacionUsuario.objects.get(id=pk)
    if request.method == 'GET':
        form = PerfilForm(instance=perfil)
    else:
        form = PerfilForm(request.POST,instance=perfil)
        if form.is_valid():
            form.save()
        return redirect('perfil:perfil_list')
    return render(request, 'perfiles/perfiles_edit.html', {'form':form}) 