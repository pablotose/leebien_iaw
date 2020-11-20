from django.core.management.base import BaseCommand, CommandError
from catalogo.models import Libro
import requests
import json

OPENLIBRARY = 'https://openlibrary.org/isbn/' 

class Command(BaseCommand):
	help = 'Inserta valores en la tabla Libro segun el ISBN que introduzca el usuario'

	def add_arguments(self , parser):
		parser.add_argument('isbn_13', nargs='+', type=str)

	def handle(self, *args, **options):
		for isbn_13 in options['isbn_13']:
			r = requests.get(OPENLIBRARY + isbn_13 + '.json')
			print (r.url)
			#b = json.dumps(r)
			a = json.loads(r.text)
			b = a['title' ] , a['isbn_13']
			insert = Libro(titulo=b[0] , ISBN=b[1])
			insert.save()

