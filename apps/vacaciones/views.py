from django.shortcuts import render,redirect
from apps.vacaciones.forms import VacacionesForm
from apps.vacaciones.models import Vacaciones
from datetime import datetime,timezone, date, timedelta

# Create your views here.
def solicitar(request):
    user = request.user.id
    if Vacaciones.objects.filter(usuario_id=user).exists():
        return redirect('vacaciones:mostrar')

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
    if Vacaciones.objects.filter(usuario_id=user).exists():
        vacaciones = Vacaciones.objects.get(usuario_id=user)
        if vacaciones.status == "Activa":
            dias_consumidos = (datetime.now(timezone.utc)-vacaciones.fecha_inicio).days
            dias_restantes = vacaciones.nro_dias - dias_consumidos
            if dias_restantes <= 0:
                vacaciones.status = "Finalizada"
                vacaciones.save()
            return render(request,'vacaciones/mostrar.html',{'vacaciones':vacaciones, 'dias_consumidos':dias_consumidos,'dias_restantes':dias_restantes})    
    else:
        vacaciones = Vacaciones.objects.filter(usuario_id=user)  
    return render(request,'vacaciones/mostrar.html',{'vacaciones':vacaciones})

def iniciar(request,pk):
    vacaciones = Vacaciones.objects.get(id=pk)
    vacaciones.status = "Activa"
    vacaciones.fecha_inicio = datetime.now(timezone.utc)
    vacaciones.save()
    return redirect('vacaciones:mostrar')
