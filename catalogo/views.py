from django.shortcuts import render

# Create your views here.
from .models import Libro , Genero , Autor , Disponibilidad
from django.views import generic
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/accounts/login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
    
def index(request):
    """
    Función vista para la página inicio del sitio.
    """
    # Genera contadores de algunos de los objetos principales
    num_libros=Libro.objects.all().count()
    num_disponibles=Disponibilidad.objects.all().count()
    # Libros disponibles (status = 'a')
    num_instances_available=Disponibilidad.objects.all().count()
    num_autores=Autor.objects.count()  # El 'all()' esta implícito por defecto.
    
    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'index.html',
        context={'num_libros':num_libros,'num_disponibles':num_disponibles,'num_autores':num_autores},
    )

class BookListView(generic.ListView):
    model = Libro
    template_name = 'catalog/lista_libros.html'
    context_object_name = 'lista_libros'
    paginate_by = 10
    #def get_queryset(self):
    #    return Libro.objects.filter(title_icontains='mierda')[:5]

class BookDetailView(generic.DetailView):
    model = Libro
    template_name = 'catalog/detalle_libro.html'
    context_object_name = 'libro'

class AutoListView(generic.ListView):
    model = Autor
    template_name = 'catalog/lista_autores.html'
    context_object_name = 'lista_autores'

class AutoDetailView(generic.DetailView):
    model = Autor
    template_name = 'catalog/detalle_autor.html'
    context_object_name = 'Autor'