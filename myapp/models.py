from django.db import models

class Carrera(models.Model):
    nombre = models.CharField(max_length=100)
    duracion = models.IntegerField(help_text="Duración en años")

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'carrera'


class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    edad = models.IntegerField()
    carrera = models.ForeignKey(
        Carrera,
        on_delete=models.CASCADE,
        related_name="estudiantes",
        null=True,  # permite valores NULL en la base de datos
        blank=True  # permite que sea opcional en formularios/Django Admin
    )

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'estudiante'
