from django.contrib import admin

from .models import UsuarioAlumnos,Seccion, Grado,Estadisticas,estadisticasPreguntas,repPreguntas,respuestas,temas,areas,ejemplos,videos,imagens
# Register your models here.

admin.site.register(UsuarioAlumnos),
admin.site.register(Seccion),
admin.site.register(Grado),
admin.site.register(Estadisticas),
admin.site.register(estadisticasPreguntas),
admin.site.register(repPreguntas),
admin.site.register(respuestas),
admin.site.register(temas),
admin.site.register(areas),
admin.site.register(ejemplos),
admin.site.register(videos),
admin.site.register(imagens)


