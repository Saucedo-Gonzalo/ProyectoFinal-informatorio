
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect, get_object_or_404

from apps.noticias.models import Noticia,Comentario


def staff_colaborador_autor(view_func):
    def permisos(request, *args, **kwargs):
        noticia_id = kwargs.get('pk')  # Obtener el ID de la noticia de los parámetros de la URL
        noticia = get_object_or_404(Noticia, pk=noticia_id)


        if request.user == noticia.autor or request.user.is_staff or request.user.groups.filter(name='colaborador').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('permisoDenegado')  
    return permisos

def staff_colaborador_autor_comentario(view_func):
    def permisos(request, *args, **kwargs):
        comentario_id = kwargs.get('pk') 
        comentario = get_object_or_404(Comentario, pk=comentario_id)

        if request.user == comentario.usuario or request.user.is_staff or request.user.groups.filter(name='colaborador').exists():
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


