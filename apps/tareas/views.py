from django.shortcuts import render,redirect
from apps.tareas.forms import TareaForm
from apps.tareas.models import Tarea
from datetime import datetime,timezone, date, timedelta
from django.core.paginator import Paginator

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

def mostrar_tarea(request,pk):
    tarea = Tarea.objects.get(id=pk)
    return render(request,'tareas/tareas_info.html',{'tarea':tarea})

def eliminar_tarea(request,pk):
    tarea = Tarea.objects.get(id=pk)
    tarea.delete()
    return redirect('tarea:listar_tareas')

def modificar_tarea(request,pk):
    tarea = Tarea.objects.get(id=pk)
    formu_tarea = TareaForm()
    if request.method == 'POST':
        formu_tarea = TareaForm(data=request.POST,instance=tarea)
        if formu_tarea.is_valid():
            tarea.save()
            #resultado = listar_tarea(pk)
            #return resultado
            return redirect('tarea:listar_tareas')
        else:
            print(formu_tarea.errors)
    else:
        #formu_tarea = TareaForm()
        return render(request,'tareas/tareas_edit_form.html',{'formu_tarea':formu_tarea})

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
    lista_tareas = Tarea.objects.filter(usuario_id=user)
    search = request.GET.get('search')
    if search:
        tareas = Tarea.objects.filter(nombre_tarea__icontains=search,usuario=request.user)
    else:
        paginator = Paginator(lista_tareas,5)
        pagina = request.GET.get('page')
        tareas = paginator.get_page(pagina)
        #contexto = {'tareas' : tareas}

    return render(request,'tareas/tareas_list.html',{'tareas' : tareas})

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

def horas(request):
    user= request.user.id  
    hoy = datetime.now(timezone.utc).date()
    lista_tareas_dia = Tarea.objects.filter(usuario_id=user, tiempo_fin__date= hoy)
    lista_tareas_sem = Tarea.objects.filter(usuario_id=user, tiempo_fin__date__range = (hoy - timedelta(days = 7), hoy))
    lista_tareas_mes = Tarea.objects.filter(usuario_id=user, tiempo_fin__year = hoy.year, tiempo_fin__month= hoy.month)
    paginator = Paginator(lista_tareas_dia,5)
    pagina = request.GET.get('page')
    tareas_dia = paginator.get_page(pagina)
    paginator = Paginator(lista_tareas_sem,5)
    pagina = request.GET.get('page')
    tareas_sem = paginator.get_page(pagina)
    paginator = Paginator(lista_tareas_mes,5)
    pagina = request.GET.get('page')
    tareas_mes = paginator.get_page(pagina)
    return render(request,'tareas/tareas_horas.html',{'tareas_dia' : tareas_dia, 'tareas_sem' : tareas_sem, 'tareas_mes' : tareas_mes})