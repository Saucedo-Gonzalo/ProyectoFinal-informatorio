from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import View
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import views as auth
from .forms import RegistroForm


# Create your views here.


class registrarse(CreateView):
    form_class = RegistroForm #toma el modelo definido en forms.
    
    success_url = reverse_lazy('usuarios:loguearse') #redirige al login luego del registro exitoso.
	
    template_name = 'usuarios/registrarse.html'


# Create your views here.
def loguearse(request):
    return render(request,'usuarios/loguearse.html')


class CustomPasswordResetCompleteView(auth.PasswordResetCompleteView):
    template_name = 'usuarios/reestablecerPassword/password_reset_complete.html'

    def get(self, request, *args, **kwargs):
        return redirect('usuarios:loguearse')  # Redirige a la vista 'usuarios:login'
