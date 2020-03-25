from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from app.forms import Formulario_Usuario,Formulario_Datos_Perfil
from app.models import InformacionUsuario

def index(request):
    user= request.user.id
    perfil = InformacionUsuario.objects.get(user_id=user)
    contexto = {'perfil' : perfil}
    return render(request,'app/index.html', contexto)

def registro(request):
    estado_registro = False
    if request.method == 'POST':
        formu_usuario = Formulario_Usuario(data=request.POST)
        formu_perfil = Formulario_Datos_Perfil(data=request.POST)
        if formu_usuario.is_valid() and formu_perfil.is_valid():
            usuario = formu_usuario.save()
            usuario.set_password(usuario.password)
            usuario.save()
            perfil = formu_perfil.save(commit=False)
            perfil.user = usuario
            if 'foto_de_perfil' in request.FILES:
                perfil.foto_de_perfil = request.FILES['foto_de_perfil']
            perfil.save()
            estado_registro = True
        else:
            print(formu_usuario.errors,formu_perfil.errors)
    else:
        formu_usuario = Formulario_Usuario()
        formu_perfil = Formulario_Datos_Perfil()
    return render(request,'app/registro.html',
                          {'formu_usuario':formu_usuario,
                           'formu_perfil':formu_perfil,
                           'estado_registro':estado_registro})

def ingreso_usuario(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        contraseña = request.POST.get('contraseña')
        token = authenticate(username=usuario, password=contraseña)
        if token:
            login(request,token)
            return HttpResponseRedirect(reverse('index'))
        else:
            messages.error(request,'usuario o contraseña incorrecto')
            return render(request, 'app/login.html', {})
    else:
        return render(request, 'app/login.html', {})

def salir(request):
    logout(request)
    return HttpResponseRedirect(reverse('ingreso'))