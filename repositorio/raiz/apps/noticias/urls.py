
from django.urls import path
from . import views

app_name='noticias'

urlpatterns = [
    # #URL CRUD'S

    #create
    path('agregarNoticia/', views.agregarNoticia, name='agregarNoticia'),
    path('agregarComentario/<int:pk>/', views.agregarComentario, name='agregarComentario'),

    #read
    path('listarNoticias/', views.listarNoticias, name='listarNoticias'),
    path('buscarNoticias/', views.buscarNoticias, name='buscarNoticias'),
    path('mostrarNoticia/<int:pk>/', views.mostrarNoticia, name='mostrarNoticia'),

    # #update
    path('modificarNoticia/<int:pk>/', views.modificarNoticia.as_view(), name='modificarNoticia'),

    #delete
    path('eliminarNoticia/<int:pk>/', views.eliminarNoticia, name='eliminarNoticia'),
    path('eliminarComentario/<int:pk>', views.eliminarComentario, name='eliminarComentario'),

]