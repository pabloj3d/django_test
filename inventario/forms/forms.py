from django import forms
from django.contrib.auth.models import User
from inventario.models import EquipoUsuario, Equipo
from django.db import models

class AsignarEquipoForm(forms.Form):
    usuario = forms.ModelChoiceField(queryset=User.objects.filter(
        ~models.Exists(EquipoUsuario.objects.filter(usuario=models.OuterRef('pk')))
    ))
    equipo = forms.ModelChoiceField(queryset=Equipo.objects.all())