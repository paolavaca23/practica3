from django.contrib import admin
from .models import *
# Register your models here.
class CarreraInline(admin.TabularInline):
    model = Carrera
    extra = 1
    autocomplete_fields = ('facultad',)


class CarreraAdmin(admin.ModelAdmin):
    list_display = ('nombre_carrera', 'cod_Carrera', 'duracion', 'is_active', 'facultad')
    search_fields = ('nombre_carrera', 'cod_Carrera')
    autocomplete_fields = ('facultad',)
    list_filter = ('is_active', 'facultad')
    ordering = ('nombre_carrera',)

class MateriaAdmin(admin.ModelAdmin):
    list_display = ('nombre_materia', 'cod_Materia', 'nivel', 'is_active', 'carrera')
    search_fields = ('nombre_materia', 'cod_Materia')
    list_filter = ('is_active', 'nivel', 'carrera')
    ordering = ('nombre_materia',)
    
class FacultadAdmin(admin.ModelAdmin):
    list_display = ('nombre_facultad', 'cod_Facultad', 'ubicacion', 'is_active')
    search_fields = ('nombre_facultad', 'cod_Facultad')
    list_filter = ('is_active',)
    ordering = ('nombre_facultad',)
    inlines = [CarreraInline]

class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'cod_Estudiante', 'email', 'fecha_inscripcion', 'fecha_nacimiento', 'carrera', 'is_active')
    search_fields = ('nombre', 'apellido', 'cod_Estudiante', 'email')
    autocomplete_fields = ('carrera',)
    list_filter = ('is_active', 'carrera')
    ordering = ('apellido', 'nombre')

class Programar_MateriasAdmin(admin.ModelAdmin):
    list_display = ('subject','student', 'fecha_programacion', 'is_active')

admin.site.register(Facultad, FacultadAdmin)
admin.site.register(Carrera, CarreraAdmin)
admin.site.register(Estudiante, EstudianteAdmin)
admin.site.register(Materia, MateriaAdmin)
admin.site.register(Programar_Materias, Programar_MateriasAdmin)