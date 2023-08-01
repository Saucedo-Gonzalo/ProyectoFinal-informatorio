
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect, get_object_or_404

from apps.noticias.models import Noticia

def staff_o_colaborador(view_func):
    def permisos(request, *args, **kwargs):
        if request.user.is_staff or request.user.groups.filter(name='colaborador').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('permisoDenegado')  
    return permisos

def staff_colaborador_autor(view_func):
    def permisos(request, *args, **kwargs):
        noticia_id = kwargs.get('pk')  # Obtener el ID de la noticia de los parámetros de la URL
        noticia = get_object_or_404(Noticia, pk=noticia_id)
        if request.user == noticia.autor or request.user.is_staff or request.user.groups.filter(name='colaborador').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('permisoDenegado')  
    return permisos

def staff(view_func):
    def permisos(request, *args, **kwargs):
        if request.user.is_staff:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('permisoDenegado')  
    return permisos


# def es_autor(view_func):
#     def permisos(request, *args, **kwargs):
#         noticia_id = kwargs.get('pk')  # Obtener el ID de la noticia de los parámetros de la URL
#         noticia = get_object_or_404(Noticia, pk=noticia_id)

#         # Verificar si el usuario actual es el creador de la noticia
#         if request.user == noticia.autor:
#             return view_func(request, *args, **kwargs)
#         else:
#             return redirect('noticias:listar')  
#     return permisos


