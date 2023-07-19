
from django.urls import path
from . import views

app_name='noticias'

urlpatterns = [
    path('listar/', views.Listar, name='listar_noticias'),
    path('listarPorFecha/', views.ListarporFecha, name='listar_noticiasporFecha'),
    path('MostrarNoticia/<int:pk>/', views.DetalleNoticia.as_view(), name='MostrarNoticia'),
    path('listarPatronales/', views.ListarPatronales, name='listar_noticiasPatronales'),
    path('listarSociales/', views.ListarSociales, name='listar_noticiasSociales'),
    path('add_comentario/<int:pk>', views.Agregar_Comentario, name="agregar_comentario"),
    path('delete_comentario/<int:pk>', views.Eliminar_Comentario, name="eliminar_comentario"),
]