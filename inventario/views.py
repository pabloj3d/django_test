from django.db import models
from django.shortcuts import render
from .models import Equipo, EquipoUsuario
from django.shortcuts import redirect
from inventario.forms.forms import AsignarEquipoForm
from django.contrib.auth.models import User
from django.utils import timezone


def lista_equipos(request):
    equipos = Equipo.objects.all()
    equipos_asignados = EquipoUsuario.objects.values_list('equipo', flat=True)
    return render(request, 'equipos.html', {'equipos': equipos, 'equipos_asignados': equipos_asignados})

def asignar_equipo(request, equipo_id):
    equipo = Equipo.objects.get(id=equipo_id)
    if request.method == 'POST':
        form = AsignarEquipoForm(request.POST)
        if form.is_valid():

            usuario_id = form.cleaned_data['usuario'].id
            usuario = User.objects.get(id=usuario_id)
            
            equipo_usuario = EquipoUsuario.objects.create(
                equipo=equipo,
                usuario=usuario,
                fecha_asignacion=timezone.now(),
                fecha_entrega=timezone.now()
            )
            return redirect('asignaciones')
    else:
        form = AsignarEquipoForm()

    usuarios_disponibles = User.objects.filter(
        ~models.Exists(EquipoUsuario.objects.filter(usuario=models.OuterRef('pk')))
    )

    equipos_disponibles = Equipo.objects.exclude(id__in=EquipoUsuario.objects.values_list('equipo', flat=True))

    return render(request, 'asignar_equipos.html', {'form': form, 'usuarios_disponibles': usuarios_disponibles, 'equipos_disponibles': equipos_disponibles})

def lista_asignaciones(request):
    asignaciones = EquipoUsuario.objects.all()
    return render(request, 'asignaciones.html', {'asignaciones': asignaciones})

def desvincular_equipos_asignados(request, asignacion_id):
    asignacion = EquipoUsuario.objects.get(id=asignacion_id)
    if request.method == 'POST':
        asignacion.delete()
        return redirect('asignaciones')
    else:
        return render(request, 'asignaciones.html', {'asignacion': asignacion})
