from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import EmailMessage
from django.template.loader import render_to_string



def Home(request):
    # Lista de objetivos del 1 al 17
    objetivos = list(range(1, 18))
    return render(request, 'home.html', {'objetivos': objetivos})

def pagObjetivo(request, numObjetivo):
    template_name = f'objetivos/p{numObjetivo}.html'
    return render(request, template_name)

def Contacto(request):
    return render(request,'contacto/contacto.html')


def emailContacto(request):
    if request.method == 'POST':
        nombre=request.POST['nombre']
        email=request.POST['email']
        subject=request.POST['subject']
        mensaje=request.POST['mensaje']

        template = render_to_string('contacto/emailContacto.html', {
            'nombre': nombre,
            'email': email,
            'mensaje':mensaje,
        })

        email = EmailMessage(
            subject,
            template,
            settings.EMAIL_HOST_USER,
            ['ods2030blog@gmail.com']  #correo al cual llegará

        )

        email.fail_silenty = False
        email.send()

        messages.success(request, 'Se ha enviado tu correo')
        return redirect('contacto')
    else:
         # Si la solicitud no es del tipo POST, redirige a otra página o muestra un mensaje de error.
        messages.error(request, 'Error: Método no permitido.')
        return HttpResponseRedirect('/')  # Redirige al usuario a la página de inicio u otra página que desees