from django.conf.urls import url , include
from django.urls import path


from . import views


urlpatterns = [
    url(r'^libro/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='libro'),
    url(r'^autores/$', views.AutoListView.as_view(),  name='autores'),
    path('accounts/', include('django.contrib.auth.urls')),


]