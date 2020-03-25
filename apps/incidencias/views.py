from django.conf import settings
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import Incidencia
from .forms import IncidenciaForm
from app.models import InformacionUsuario

def incidencias_list_view(request):
    user= request.user.id
    perfil = InformacionUsuario.objects.get(user_id=user)
    queryset = Incidencia.objects.filter(usuario_id=user)
    context = {
        "incidencias_list": queryset,
        "perfil": perfil,
    }
    return render(request, "incidencias_list.html", context)

def incidencia_crear(request):
    user= request.user.id
    user_email = request.user.email
    perfil = InformacionUsuario.objects.get(user_id=user)
    if request.method == 'POST':
        form = IncidenciaForm(data=request.POST)
        if form.is_valid():
            incidencia = form.save(commit=False)
            incidencia.usuario_id = user
            incidencia.save()
            subject = "Ubicutus - has reportado una incidencia"
            message = "Se ha reportado la incidencia " + incidencia.titulo + " esta tiene un estatus por revisar"
            from_email = settings.EMAIL_HOST_USER
            addresses = [user_email, settings.EMAIL_HOST_USER]
            send_mail(subject, message, from_email, addresses, fail_silently=True)
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