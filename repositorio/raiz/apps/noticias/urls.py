
from django.urls import path
from . import views

app_name='noticias'

urlpatterns = [
    # #URL CRUD'S

    #create
    path('agregar/', views.agregarNoticia, name='agregarNoticia'),

    #read
    path('listar/', views.listarNoticias, name='listarNoticias'),
    # path('listarPorFecha/', views.listarPorFecha, name='listarPorFecha'),
    # path('listarPorObjetivo/<int:pk>', views.listarPorObjetivo, name='listarPorObjetivo'),
    # path('Mostrar/<int:pk>/', views.detalleNoticia.as_view(), name='detalleNoticia'),

    # #update
    path('modificarNoticia/<int:pk>/', views.modificarNoticia.as_view(), name='modificarNoticia'),
    # path('modificarComentario/<int:pk>', views.modificarComentario, name='modificarComentario'),

    #delete
    path('eliminarNoticia/<int:pk>/', views.eliminarNoticia, name='eliminarNoticia'),
    # path('eliminarComentario/<int:pk>', views.eliminarComentario, name='eliminarComentario'),

]