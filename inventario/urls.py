from django.urls import path
from . import views

urlpatterns = [
    path("equipos/", views.lista_equipos, name="equipos"),
    path('asignaciones/', views.lista_asignaciones, name='asignaciones'),
    path('asignar-equipos/<int:equipo_id>/', views.asignar_equipo, name='asignar_equipo'),
    path('asignaciones/<int:asignacion_id>/', views.desvincular_equipos_asignados, name='desvincular_equipos_asignados'),
]
