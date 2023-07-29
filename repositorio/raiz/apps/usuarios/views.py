from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import update_session_auth_hash

from django.views.generic import CreateView,FormView
from django.urls import reverse_lazy
from django.contrib.auth import views as auth
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


# asi lo hago asi envia dos emails, uno con etiquetas html y otro sin
class CustomPasswordResetCompleteView(auth.PasswordResetCompleteView):
    #template_name = 'usuarios/reestablecerPassword/password_reset_complete.html'

    def get(self, request, *args, **kwargs):
        return redirect('usuarios:loguearse')  # Redirige a la vista 'usuarios:login'
    

    
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

# class CustomPasswordResetConfirmView(auth.PasswordResetConfirmView):
#     form_class = CustomPasswordResetConfirmViewForm

# def password_change(request):
#     if request.method == 'POST':
#         form = PasswordChangeForm(request.user, request.POST)
#         if form.is_valid():
#             user = form.save()
#             update_session_auth_hash(request, user)  # Actualiza la sesión del usuario para mantenerlo autenticado
#             return redirect('home')  # Cambia esto a la ruta a la que quieres redirigir después de cambiar la contraseña
#     else:
#         form = PasswordChangeForm(request.user)
#     return render(request, 'usuarios/cambiarPassword/password_change.html', {'form': form})

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