
#def sacar_libros(codigo):
#	a = "https://openlibrary.org/isbn/


#import json 
#f = open("https://openlibrary.org/books/OL30559383M.json", "r")
#contenido = f.read()
#sacarjson =json.loads(contenido)

#print (sacarjson)

import requests
import json
r = requests.get('https://openlibrary.org/isbn/9788441525139.json')
#b = json.dumps(r)
a = json.loads(r.text)
b = a['title' ] ,  a['isbn_13'] , a['publish_date']
#claves = a.values()
#print (b[0] , b[1] , b[2])
from catalogo.models import Libro 
insert = Libro(titulo=b[0] ,  ISBN=b[1])
insert.save()
