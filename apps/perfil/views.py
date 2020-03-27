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
   

def perfil_edit(request):
    user= request.user.id
    perfil = InformacionUsuario.objects.get(user_id=user)
    if request.method == 'GET':
        form = PerfilForm(instance=perfil)
    else:
        form = PerfilForm(request.POST,instance=perfil)
        if form.is_valid():
            new_perfil = form.save(commit=False)
            new_perfil.user_id = user
            if 'foto_de_perfil' in request.FILES:
                new_perfil.foto_de_perfil = request.FILES['foto_de_perfil']
            new_perfil.save()
        return redirect('perfil:perfil_list')
    return render(request, 'perfiles/perfiles_edit.html', {'form':form}) 