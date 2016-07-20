from django.conf.urls import url
from . import views

app_name ='App'
urlpatterns = [

    url(r'^indexA/', views.indexA, name = "indexA"),
    url(r'^detailA/(?P<autor_id>[0-9]+)/$', views.detailA, name='detailA'),
    url(r'^borrarA/(?P<autor_id>\d+)/$',  views.borrarA, name='borrarA'),
    url(r'^editarA/(?P<autor_id>\d+)/$',  views.actualizarA, name='editarA'),
    url(r'^crearA/', views.crearA, name = "crearA"),

    #/Libros/2/
    url(r'^$', views.index, name='index'),
    url(r'^(?P<libro_id>[0-9]+)/$', views.detalle, name='detalle'),
    url(r'^borrar/(?P<libro_id>\d+)/$',  views.borrar, name='borrar'),
    url(r'^edita/(?P<libro_id>\d+)/$',  views.actualizar, name='edita'),
    url(r'^crear/', views.crear, name = "crear"),

]
