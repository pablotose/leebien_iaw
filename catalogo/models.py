from django.db import models
import uuid

# Create your models here.
class Genero(models.Model):

	name = models.CharField(max_length=80)
	#identificador = models.AutoField()

	def __str__(self):
		return self.name


class Libro(models.Model):

	titulo = models.CharField(max_length=200)

	Idioma = models.CharField(max_length=8)

	genero = models.ManyToManyField(Genero, help_text="Seleccione un genero para este libro")

	ISBN = models.CharField(max_length=13)

	Fecha_Publicacion = models.DateField(null=True)

	Resumen = models.CharField(max_length=1000)

	Autor = models.ForeignKey('Autor' , on_delete=models.SET_NULL, null=True)

	Precio = models.PositiveIntegerField(default=0)

	def __str__(self):
		return self.titulo

	def display_genero(self):
		return ', '.join([ genero.name for genero in self.genero.all()[:3] ])


class Autor(models.Model):

	Nombre = models.CharField(max_length=60)

	Biografia = models.CharField(max_length=1000)

	Genero = models.CharField(max_length=80,) #choices=array_choice)

	def __str__(self):
		return self.Nombre



class Disponibilidad(models.Model):

	ids = models.UUIDField(primary_key=True, default=uuid.uuid4)

	libro_disponibles = models.ForeignKey('Libro', on_delete=models.SET_NULL, null=True) 


	numero_unidades = models.PositiveIntegerField(default=0)

	LOAN_STATUS = (
		('s', 'En Stock'),
		('a', 'Agotado'),
	)
	estado = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='s', help_text='Disponibilidad del libro')

	def __str__(self):
		return str(self.libro_disponibles)
