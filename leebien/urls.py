"""leebien URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.urls import include
from catalogo import views
from django.conf.urls import url
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from rest_framework import routers



from catalogo.api import views


router = routers.DefaultRouter()
router.register(r'Libro', views.LibroViewSet)
router.register(r'Autor', views.AutorViewSet)


urlpatterns = [
	url(r'^$', views.index, name='index'),
    path('admin/', admin.site.urls),
    #path('index', views.index, name='index'),
    url(r'^libros/$', views.BookListView.as_view() ,  name='libros'),
    url(r'^libro/(?P<pk>\d+)$', login_required(views.BookDetailView.as_view()), name='detalle_libro'),
    url(r'^autores/$', views.AutoListView.as_view(),  name='autores'),
    url(r'^autors/(?P<pk>\d+)$', login_required(views.AutoDetailView.as_view()), name='detalle_autor'),
    url(r'^signup/$', views.signup, name='signup'),
    url('auth/', views.auth, name='auth'),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls' , namespace = 'rest_framework')),
    url(r'^search/$', views.search, name='search')


]	


# Use include() to add paths from the catalog application 
from django.urls import include

urlpatterns += [
    path('catalogo/', include('catalogo.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]