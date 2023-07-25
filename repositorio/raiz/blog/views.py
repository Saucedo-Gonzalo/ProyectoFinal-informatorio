from django.http import HttpResponse
from django.shortcuts import render



def Home(request):
    # Lista de objetivos del 1 al 17
    objetivos = list(range(1, 18))
    return render(request, 'home.html', {'objetivos': objetivos})

def pagObjetivo(request, numObjetivo):
    template_name = f'objetivos/p{numObjetivo}.html'
    return render(request, template_name)

def Contacto(request):
    return render(request,'contacto.html')