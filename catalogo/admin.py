from django.contrib import admin
from .models import Autor, Libro, Genero, Disponibilidad
#admin.site.register(Libro)
#admin.site.register(Autor)
admin.site.register(Genero)
#admin.site.register(Disponibilidad)

class AutorAdmin(admin.ModelAdmin):
	list_display = ('Nombre', 'Biografia', 'Genero',)

admin.site.register(Autor, AutorAdmin)

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
	list_display = ('titulo', 'Autor', 'display_genero')

@admin.register(Disponibilidad)
class DisponibilidadAdmin(admin.ModelAdmin):
	list_filter = ('estado', 'numero_unidades')	
	
		