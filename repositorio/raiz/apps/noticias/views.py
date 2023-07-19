from django.shortcuts import render

#VER QUE NO SIRVE
from ast import Not
from datetime import date
from email import message
from gc import get_objects
from symtable import Class
from urllib import response
from django.shortcuts import render,get_object_or_404,redirect
from .models import Noticia
from django.core.paginator import Paginator
from django.views.generic import DetailView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from django.http import HttpResponseRedirect,HttpResponse


from .models import Noticia,Comentario

# Create your views here.

def Listar(request):
    #Creo el diccionario para pasar datos al templeate
    #ctx={}
    #Buscar las noticias de la BD
    todas=Noticia.objects.all()
    #Buscar lo que quiera de la BD
    #ctx['notis']=todas
    
    paginator=Paginator(todas,4)
    pagina= request.GET.get("page") or 1
    posts =paginator.get_page(pagina)
    currents_page= int(pagina)
    paginas=range(1,posts.paginator.num_pages+1)
    
    return render(request,'noticias/listar_noticias.html',{"posts":posts,"paginas":paginas,"currents_page":currents_page})
    #return render(request,'noticias/listar_noticias.html',ctx)

def ListarporFecha(request):
    todas=Noticia.objects.all().order_by('-creado')
    
    paginator=Paginator(todas,4)
    pagina= request.GET.get("page") or 1
    posts =paginator.get_page(pagina)
    currents_page= int(pagina)
    paginas=range(1,posts.paginator.num_pages+1)
    
    return render(request,'noticias/listar_noticias.html',{"posts":posts,"paginas":paginas,"currents_page":currents_page})


#def MostrarNoticia(request):
    #ctx={}
    #noticia=Noticia.objects.all()
    #ctx['noticia']=noticia
    #return render(request,'noticias/Pag_Noticia.html',ctx)
    
class DetalleNoticia(LoginRequiredMixin,DetailView):
    model=Noticia
    template_name='noticias/Detalle_Noticia.html'

def ListarPatronales(request):
    todas=Noticia.objects.all().filter(categoria=2)
    
    paginator=Paginator(todas,4)
    pagina= request.GET.get("page") or 1
    posts =paginator.get_page(pagina)
    currents_page= int(pagina)
    paginas=range(1,posts.paginator.num_pages+1)
    
    return render(request,'noticias/listar_noticias.html',{"posts":posts,"paginas":paginas,"currents_page":currents_page})

def ListarSociales(request):
    todas=Noticia.objects.all().filter(categoria=3)
    
    paginator=Paginator(todas,4)
    pagina= request.GET.get("page") or 1
    posts =paginator.get_page(pagina)
    currents_page= int(pagina)
    paginas=range(1,posts.paginator.num_pages+1)
    
    return render(request,'noticias/listar_noticias.html',{"posts":posts,"paginas":paginas,"currents_page":currents_page})


def Agregar_Comentario(request,pk):
	texto_comentario = request.POST.get('coment')
	
	#Forma 1 (es la mejor para este caso)
	noti = Noticia.objects.get(pk = pk)

	c = Comentario.objects.create(noticia = noti, texto = texto_comentario, usuario = request.user)

	return HttpResponseRedirect(reverse_lazy('noticias:MostrarNoticia' , kwargs={'pk':pk}))


def Eliminar_Comentario(request,pk):
    comentario=get_object_or_404(Comentario,id=pk)
    if comentario.usuario==request.user:
        comentario.delete()
        return HttpResponseRedirect(reverse_lazy('noticias:listar_noticias'))
    else:
        response=HttpResponse("NO TIENES PERMISO PARA ESTA ACCION")
        response.status_code=403
        return response
        

