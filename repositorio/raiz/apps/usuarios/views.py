
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.views.generic import CreateView,FormView
from django.urls import reverse_lazy
from django.contrib.auth import views as auth
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from apps.usuarios.models import Usuario
from .forms import RegistroForm
# from django.core.mail import send_mail
# from django.template.loader import render_to_string
# from django.utils.http import urlsafe_base64_encode
# from django.utils.encoding import force_bytes
# from django.contrib.auth import get_user_model
# from django.contrib.auth.tokens import default_token_generator


# Create your views here.


class registrarse(CreateView):
    form_class = RegistroForm #toma el modelo definido en forms.
    
    success_url = reverse_lazy('usuarios:loguearse') #redirige al login luego del registro exitoso.
	
    template_name = 'usuarios/registrarse.html'


# Create your views here.
def loguearse(request):
    return render(request,'usuarios/loguearse.html')


class CustomPasswordResetCompleteView(auth.PasswordResetCompleteView):

    def get(self, request, *args, **kwargs):
        return redirect('usuarios:password_success')  # Redirige a la vista 'usuarios:loguearse' luego del mensaje
    

    
# asi lo hago asi envia dos emails, uno con etiquetas html y otro sin
# class CustomPasswordResetView(auth.PasswordResetView):
#     def form_valid(self, form):
#         # Obtener el correo electrónico del formulario
#         email = form.cleaned_data['email']
        
#         # Obtener el modelo de usuario personalizado
#         User = get_user_model()

#         try:
#             # Obtener el usuario asociado al correo electrónico proporcionado
#             user = User.objects.get(email=email)

#             # Generar el contexto para la plantilla del correo electrónico
#             uid = urlsafe_base64_encode(force_bytes(user.pk))
#             token = default_token_generator.make_token(user)
#             protocol = 'http'  # Usar 'https' si tienes SSL configurado
#             domain = self.request.get_host()
#             # Renderizar el contenido del correo electrónico con el contexto generado
#             email_content = render_to_string(
#                 self.email_template_name,
#                 {
#                     'user': user,
#                     'uid': uid,
#                     'token': token,
#                     'protocol': protocol,
#                     'domain': domain,
#                 }
#             )
#             # Enviar el correo electrónico
#             send_mail(
#                 'Recuperación de contraseña para tu cuenta en ODS2030 Blog',
#                 '',  # Deja el cuerpo del correo electrónico vacío, ya que está en la plantilla HTML
#                 'ods2030blog@gmail.com',  # Dirección de correo electrónico del remitente (puedes cambiarlo)
#                 [email],  # Lista de destinatarios, en este caso, solo un correo electrónico
#                 html_message=email_content,  # Especificar el contenido como HTML
#                 fail_silently=False,  # Cambiar a True si deseas que los errores no generen excepciones
#             )
#         except User.DoesNotExist:
#             # El usuario no existe, se puede manejar el error o simplemente ignorarlo
#             pass

#         # Llamar al método form_valid de la clase padre para continuar con la lógica de redirección
#         return super().form_valid(form)



class password_change(FormView):
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
    
def listarUsuarios(request):
    usuarios_list = Usuario.objects.all()   # Muestra todas las noticias

    # Configurar la paginación: 10 usuarios por página
    paginator = Paginator(usuarios_list, 15)
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



def eliminarUsuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk) #la funcion guarda en su variable pk el id de la noticia para luego borrarla
    usuario.delete()
    messages.success(request, 'El usuario ha sido eliminado')
    return redirect('usuarios:listarUsuarios')

def modificarUsuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)

    if request.method == 'POST':
        # Obtener los datos enviados por el formulario
        username = request.POST['username']
        email = request.POST['email']
        es_colaborador = 'es_colaborador' in request.POST

        # Actualizar el usuario con los datos modificados
        usuario.username = username
        usuario.email = email
        
        # Actualizar la pertenencia al grupo "colaborador"
        grupo_colaborador = 'colaborador'
        if es_colaborador:
            usuario.groups.add(es_colaborador)
        else:
            usuario.groups.remove(es_colaborador)
        
        usuario.save()

        # Redireccionar a la lista de usuarios o a otra página de tu elección
        return redirect('usuarios:listarUsuarios')

    # Si la petición es GET, mostrar el formulario con los datos actuales del usuario
    context = {'usuario': usuario, 'es_colaborador': usuario.groups.filter(name='colaborador').exists()}
    return render(request, 'usuarios/modificar.html', context)
