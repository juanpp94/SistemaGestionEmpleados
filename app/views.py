from django.shortcuts import render
from app.forms import Formulario_Usuario,Formulario_Datos_Perfil, Formulario_Tarea
from app.models import Tarea, User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from datetime import datetime, timedelta

def index(request):
    return render(request,'app/index.html')

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
            return HttpResponse("Usuario o contraseña erradas")
    else:
        return render(request, 'app/login.html', {})

def salir(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def agregar_tarea(request):
    iniciada = False
    tarea = 0 
    if request.method == 'POST':
        formu_tarea = Formulario_Tarea(data=request.POST)
        if formu_tarea.is_valid():
            tarea = formu_tarea.save()
            iniciada = True
        else:
            print(formu_tarea.errors)
    else:
        formu_tarea = Formulario_Tarea()
    return render(request,'app/tarea.html',
                          {'formu_tarea':formu_tarea,
                            'estado_tarea':iniciada,
                            'tarea': tarea})

def tiempo_tarea(request):
    tarea = Tarea.objects.all().last()
    current_user = request.user ##Borrar
    print(current_user) ##Borrar
    tarea.save() #Tiempo de finalizacion
    for x in Tarea.objects.all(): ## BORRAR                          
                                  ##USAR ESTO PARA  LO DE MOSTRAR TODAS LAS TAREAS Y TIEMPO
        print(x.nombre_tarea)
    print(str((tarea.tiempo_fin - tarea.tiempo_inicio).total_seconds()) + " segundos") #Borrar esto es de prueba
    return HttpResponseRedirect(reverse('index'))