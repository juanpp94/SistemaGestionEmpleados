from django.shortcuts import render,redirect
from apps.tareas.forms import TareaForm
from apps.tareas.models import Tarea
from datetime import datetime,timezone

# Create your views here.
def agregar_tarea(request):
    user = request.user.id
    tarea = 0 
    if request.method == 'POST':
        formu_tarea = TareaForm(data=request.POST)
        if formu_tarea.is_valid():
            tarea = formu_tarea.save(commit=False)
            tarea.usuario_id = request.user.id
            tarea.status = 'activa'
            tarea.save()
            return render(request,'tareas/tareas_index.html',{'tarea': tarea})
        else:
            print(formu_tarea.errors)
    else:
        formu_tarea = TareaForm()
    return render(request,'tareas/tareas_form.html',{'formu_tarea':formu_tarea})

def tiempo_tarea(request, pk):
    tarea = Tarea.objects.get(id=pk)
    tarea.tiempo_fin = datetime.now(timezone.utc)
    tiempo_total =  tarea.tiempo_total + (tarea.tiempo_fin - tarea.tiempo_inicio).total_seconds()
    segundos = tiempo_total
    tarea.tiempo_total = tiempo_total
    horas = int(segundos // 3600)
    minutos = int((segundos % 3600) // 60)
    segundos = int(segundos % 60)
    formato = '{} horas, {} minutos, {} segundos'.format(horas, minutos, segundos)
    tarea.tiempo_total_formato = formato
    tarea.save()
    
    return redirect('tarea:listar_tareas')

def listar_tarea(request):
    user= request.user.id  
    tareas = Tarea.objects.filter(usuario_id=user)
    contexto = {'tareas' : tareas}
    return render(request,'tareas/tareas_list.html',contexto)

def iniciar_tarea(request, pk):
    tarea = Tarea.objects.get(id=pk)
    tarea.tiempo_inicio = datetime.now(timezone.utc)
    tarea.save()
    return render(request,'tareas/tareas_index.html',{'tarea': tarea})

def finalizar_tarea(request, pk):
    tarea = Tarea.objects.get(id=pk)
    tarea.status = "finalizada"
    tarea.save()
    return redirect('tarea:listar_tareas')    