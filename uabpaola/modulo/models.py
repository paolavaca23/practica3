from django.db import models
from django.utils import timezone


# Create your models here.
class Carrera(models.Model):
    nombre_carrera = models.CharField(max_length=100)
    cod_Carrera = models.CharField(max_length=20, unique=True)
    duracion = models.IntegerField(help_text="Duración en años")
    is_active = models.BooleanField(default=True)
    facultad = models.ForeignKey(
        "Facultad",
        on_delete=models.CASCADE,
        related_name="carreras",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.nombre_carrera

    class Meta:
        verbose_name = "Carrera"
        verbose_name_plural = "Carreras"
        ordering = ["nombre_carrera"]


class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cod_Estudiante = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    fecha_inscripcion = models.DateField(default=timezone.now)
    fecha_nacimiento = models.DateField()
    carrera = models.ForeignKey(
        Carrera,
        on_delete=models.CASCADE,
        related_name="estudiantes",
        null=True,
        blank=True,
    )
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"
        ordering = ["apellido", "nombre"]


class Materia(models.Model):
    nombre_materia = models.CharField(max_length=100)
    cod_Materia = models.CharField(max_length=20, unique=True)
    nivel = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    carrera = models.ForeignKey(
        Carrera,
        on_delete=models.CASCADE,
        related_name="materias",
        null=True,
        blank=True,
    )
    def __str__(self):
        return self.nombre_materia

    class Meta:
        verbose_name = "Materia"
        verbose_name_plural = "Materias"
        ordering = ["nombre_materia"]


class Facultad(models.Model):
    nombre_facultad = models.CharField(max_length=100)
    cod_Facultad = models.CharField(max_length=20, unique=True)
    ubicacion = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    foto = models.ImageField(upload_to="facultad_fotos/", null=True, blank=True)

    def __str__(self):
        return self.nombre_facultad

    class Meta:
        verbose_name = "Facultad"
        verbose_name_plural = "Facultades"
        ordering = ["nombre_facultad"]


class Programar_Materias(models.Model):
    student = models.ForeignKey(
        Estudiante,
        on_delete=models.CASCADE,
        related_name="Programar",
        null=True,
        blank=True,
        verbose_name="Estudiante",
    )
    subject = models.ForeignKey(
        Materia,
        on_delete=models.CASCADE,
        related_name="Programar",
        null=True,
        blank=True,
        verbose_name="Materia",
    )
    is_active = models.BooleanField(default=True, verbose_name="¿esta activa la programacion?")
    fecha_programacion = models.DateField(default=timezone.now)
    
    def __str__(self):
        return f"{self.student} - {self.subject} - {self.fecha_programacion}"

    class Meta:
        verbose_name = "Programar Materias"
        verbose_name_plural = "Programar Materias"
        ordering = ["student", "subject"]
        unique_together = ('student', 'subject', 'fecha_programacion')