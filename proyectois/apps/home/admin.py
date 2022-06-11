from django.contrib import admin

from .models import *# Register your models here.

class respuestaInLine(admin.TabularInline):
    model = respuestas

class preguntaAdmin(admin.ModelAdmin):
    inlines = [respuestaInLine]

admin.site.register(repPreguntas,preguntaAdmin),
admin.site.register(UsuarioAlumnos),
admin.site.register(Seccion),
admin.site.register(Grado),
admin.site.register(Estadisticas),
admin.site.register(estadisticasPreguntas),
admin.site.register(respuestas),
admin.site.register(temas),
admin.site.register(areas),
admin.site.register(ejemplos),


