from django.conf.urls import url



from . import views


urlpatterns = [
    url(r'^libro/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='libro'),
    url(r'^autores/$', views.AutoListView.as_view(),  name='autores'),
    

]