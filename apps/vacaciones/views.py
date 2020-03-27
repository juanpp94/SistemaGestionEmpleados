from django.shortcuts import render,redirect
from apps.vacaciones.forms import VacacionesForm
from apps.vacaciones.models import Vacaciones
from datetime import datetime,timezone, date, timedelta

# Create your views here.
def solicitar(request):
    dias_disponibles = 19
    #vacaciones = Vacaciones.objects.filter(usuario_id=request.user.id)
    #for vacs in vacaciones:
     #   dias_disponibles = dias_disponibles - vacs.nro_dias
    #user = request.user.id
    if request.method == 'POST':
        formu_vacs = VacacionesForm(data=request.POST)
        if formu_vacs.is_valid():
            vacaciones = formu_vacs.save(commit=False)
            vacaciones.usuario_id = request.user.id
            vacaciones.status = 'Pendiente'
            vacaciones.save()
            return redirect('vacaciones:mostrar')
        else:
            print(formu_vacs.errors)
    else:
        formu_vacs = VacacionesForm()
    return render(request,'vacaciones/solicitar.html',{'formu_vacs':formu_vacs})

def mostrar(request):
    user = request.user.id
    vacs = Vacaciones.objects.filter(usuario_id=user)
    dias_consumidos = 0
    dias_restantes = 0
    for vacaciones in vacs:
        if vacaciones.status == "Activa":
            dias_consumidos = (datetime.now(timezone.utc)-vacaciones.fecha_inicio).days
            dias_restantes = vacaciones.nro_dias - dias_consumidos
            if dias_restantes <= 0:
                vacaciones.status = "Finalizada"
                vacaciones.save()    
    fin = finalizadas(user)
    return render(request,'vacaciones/mostrar.html',{'vacs':vacs,'fin':fin,'dias_consumidos':dias_consumidos,'dias_restantes':dias_restantes})

def iniciar(request,pk):
    vacaciones = Vacaciones.objects.get(id=pk)
    vacaciones.status = "Activa"
    vacaciones.fecha_inicio = datetime.now(timezone.utc)
    vacaciones.save()
    return redirect('vacaciones:mostrar')

def finalizadas(id):
    vacaciones = Vacaciones.objects.filter(usuario_id=id)
    for vacs in vacaciones:
        if vacs.status != "Finalizada" and vacs.status != "Rechazada":
            return False
    return True