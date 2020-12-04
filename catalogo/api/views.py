from rest_framework import viewsets
from catalogo.models import Libro , Autor
from catalogo.api.serializers import LibroSerializer , AutorSerializer
from catalogo.models import *
from catalogo.views import *


class LibroViewSet(viewsets.ModelViewSet):
	queryset = Libro.objects.all()
	serializer_class = LibroSerializer

class AutorViewSet(viewsets.ModelViewSet):
	queryset = Autor.objects.all()
	serializer_class = AutorSerializer
