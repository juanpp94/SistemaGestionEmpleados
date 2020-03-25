from django.shortcuts import render, redirect
from .models import Incidencia
from .forms import IncidenciaForm
from app.models import InformacionUsuario

def incidencias_list_view(request):
    user= request.user.id
    perfil = InformacionUsuario.objects.get(user_id=user)
    queryset = Incidencia.objects.filter(usuario_id=user)
    context = {
        "incidencias_list": queryset,
        "perfil": perfil
    }
    return render(request, "incidencias_list.html", context)

def incidencia_crear(request):
    user= request.user.id
    perfil = InformacionUsuario.objects.get(user_id=user)
    if request.method == 'POST':
        form = IncidenciaForm(data=request.POST)
        if form.is_valid():
            incidencia = form.save(commit=False)
            incidencia.usuario_id = user
            incidencia.save()
    else:
        form = IncidenciaForm()
    return render(request,'incidencias_form.html',{'form':form, 'perfil':perfil})

def incidencia_mostrar(request, pk):
    user= request.user.id
    perfil = InformacionUsuario.objects.get(user_id=user)
    incidencia = Incidencia.objects.get(id=pk)
    context = {'incidencia':incidencia, 'perfil':perfil}
    return render(request,'incidencia.html',context)

def incidencia_editar(request, pk):
    user= request.user.id
    perfil = InformacionUsuario.objects.get(user_id=user)
    incidencia = Incidencia.objects.get(id=pk)
    if request.method == 'GET':
        form = IncidenciaForm(instance=incidencia)
    else:
        form = IncidenciaForm(data=request.POST, instance=incidencia)
        if form.is_valid():
            incidencia = form.save(commit=False)
            incidencia.usuario_id = user
            incidencia.save()
    context = {
        'form':form, 
        'perfil':perfil
    }
    return render(request,'incidencias_form.html',context)