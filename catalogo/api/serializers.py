from rest_framework import serializers
from catalogo.models import Libro , Autor

class LibroSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Libro
		fields = ('titulo', 'Idioma', 'ISBN', 'Fecha_Publicacion', 'Resumen', 'Autor'  )

class AutorSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Autor
		fields = ('Nombre', 'Biografia', 'Genero')