from django.db import models


# Create your models here.
class Equipo(models.Model):
    referencia = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    procesador = models.CharField(max_length=50)
    memoria = models.CharField(max_length=50)
    disco = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.id} - {self.referencia}"


class EquipoUsuario(models.Model):
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    usuario = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    fecha_asignacion = models.DateField()
    fecha_entrega = models.DateField()

    def __str__(self):
        return f"{self.equipo.referencia} - {self.usuario.username}"
