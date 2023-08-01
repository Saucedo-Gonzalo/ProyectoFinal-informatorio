
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.views.generic import CreateView,FormView
from django.urls import reverse_lazy
from django.contrib.auth import views as auth
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from apps.usuarios.models import Usuario
from django.contrib.auth.models import Group
from .forms import RegistroForm
from django.db import IntegrityError
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from blog.decorators import *



class registrarse(CreateView):
    form_class = RegistroForm #toma el modelo definido en forms.
    
    success_url = reverse_lazy('usuarios:loguearse') #redirige al login luego del registro exitoso.
	
    template_name = 'usuarios/registrarse.html'

def loguearse(request):
    return render(request,'usuarios/loguearse.html')


class CustomPasswordResetCompleteView(auth.PasswordResetCompleteView):

    def get(self, request, *args, **kwargs):
        return redirect('usuarios:password_success')  # Redirige a la vista 'usuarios:loguearse' luego del mensaje
    

class password_change(LoginRequiredMixin, FormView):
    template_name = 'usuarios/cambiarPassword/password_change.html'
    form_class = SetPasswordForm
    success_url = reverse_lazy('home')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        update_session_auth_hash(self.request, form.user)
        return super().form_valid(form)
    
def password_success(request):
    return render(request,'usuarios/cambiarPassword/password_success.html') 
    
@staff 
def listarUsuarios(request):
    usuarios_list = Usuario.objects.all()   # Muestra todas las noticias

    # Configurar la paginación: 10 usuarios por página
    paginator = Paginator(usuarios_list, 10)
    page = request.GET.get('pagina')

    try:
        usuarios = paginator.page(page)
    except PageNotAnInteger:
        # Si el parámetro 'page' no es un número, mostrar la primera página
        usuarios = paginator.page(1)
    except EmptyPage:
        # Si el número de página está fuera de rango, mostrar la última página
        usuarios = paginator.page(paginator.num_pages)

    context = {'usuarios': usuarios}
    return render(request, 'usuarios/listar.html', context)


@staff  
def eliminarUsuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk) #la funcion guarda en su variable pk el id de la noticia para luego borrarla
    usuario.delete()
    messages.success(request, 'El usuario ha sido eliminado')
    return redirect('usuarios:listarUsuarios')

@login_required
def modificarUsuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)

    if request.method == 'POST':
        # Obtener los datos enviados por el formulario
        username = request.POST['username']
        email = request.POST['email']
        es_colaborador = 'es_colaborador' in request.POST

        try:
        # Actualizar el usuario con los datos modificados
            usuario.username = username
            usuario.email = email
            
            colaborador_group = Group.objects.get(name='colaborador')
            if es_colaborador:
                colaborador_group.user_set.add(usuario)
            else:
                colaborador_group.user_set.remove(usuario)
            
            usuario.save()

            # Redireccionar a la lista de usuarios o a otra página de tu elección
            return redirect('usuarios:listarUsuarios')
        except IntegrityError:
            # Si se produce una excepción de integridad debido a que el nombre de usuario ya existe, mostrar un mensaje de error.
            mensajeError = "El nombre de usuario ya está en uso. Por favor, elige otro nombre."
            context = {'usuario': usuario, 'es_colaborador': usuario.groups.filter(name='colaborador').exists(), 'mensajeError': mensajeError}
            return render(request, 'usuarios/modificar.html', context)

    # Si la petición es GET, mostrar el formulario con los datos actuales del usuario
    context = {'usuario': usuario, 'es_colaborador': usuario.groups.filter(name='colaborador').exists()}
    return render(request, 'usuarios/modificar.html', context)
