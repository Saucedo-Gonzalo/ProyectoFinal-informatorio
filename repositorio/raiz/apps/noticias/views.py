#VER QUE NO SIRVE
from django import forms
from django.shortcuts import render,get_object_or_404,redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import UpdateView, DeleteView, CreateView
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import NoticiaAgregarForm, NoticiaForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib import messages
from django.db.models import Q
from django.urls import reverse
from .models import Noticia,Comentario

#vistas CRUD
#Noticias
#create


def agregarNoticia(request):
    if request.method == 'POST':
        form = NoticiaAgregarForm(request.POST, request.FILES)
        if form.is_valid():

            noticia = form.save(commit=False)
            noticia.autor = request.user  # Asignar el usuario actual como autor de la noticia
            noticia.save()
            messages.success(request, 'Noticia modificada exitosamente.')
            return redirect('noticias:listarNoticias')
    else:
        form = NoticiaAgregarForm()
    return render(request, 'noticias/agregarNoticia.html', {'form': form})


def agregarComentario(request,pk):
	texto = request.POST.get('comentario')
	noticia = Noticia.objects.get(pk = pk)
	c = Comentario.objects.create(noticia = noticia, texto = texto, usuario = request.user)
	return redirect('noticias:mostrarNoticia' , pk=pk)



#read

def buscarNoticias(request):
    query = request.POST.get('buscar')
    noticias = None

    if query:
        noticias = Noticia.objects.filter(
            Q(titulo__icontains=query) |
            Q(cuerpo__icontains=query) |
            Q(objetivo__nombre__icontains=query) |
            Q(autor__username__icontains=query)
        )

    context = {
        'noticias': noticias
    }
    return render(request, 'noticias/listarNoticias.html', context)


def listarNoticias(request):
    noticias_list = Noticia.objects.all()

    # Configurar la paginación: 9 noticias por página
    paginator = Paginator(noticias_list, 6)
    page = request.GET.get('page')

    try:
        noticias = paginator.page(page)
    except PageNotAnInteger:
        # Si el parámetro 'page' no es un número, mostrar la primera página
        noticias = paginator.page(1)
    except EmptyPage:
        # Si el número de página está fuera de rango, mostrar la última página
        noticias = paginator.page(paginator.num_pages)

    context = {'noticias': noticias}
    return render(request, 'noticias/listarNoticias.html', context)

def mostrarNoticia(request, pk): #viene como parametro el pk que ingreso en la url
    noticia = get_object_or_404(Noticia, pk=pk)   # Muestra solo una noticia por su pk
    comentarios = noticia.mis_comentarios.all()  # Obtener todos los comentarios asociados a esta noticia
    context = {'noticia': noticia, 'comentarios': comentarios}
    return render(request, 'noticias/mostrarNoticia.html', context)

#update
class modificarNoticia(UpdateView):
    model= Noticia
    template_name= 'noticias/modificarNoticia.html'
    #form_class = NoticiaForm
    fields = ['titulo', 'cuerpo', 'imagen', 'objetivo', 'estado']
    success_url= reverse_lazy('noticias:listarNoticias')


    def form_valid(self, form):
        # Obtener el valor de los campos del formulario
        titulo = form.cleaned_data['titulo']
        cuerpo = form.cleaned_data['cuerpo']
        #autor = form.cleaned_data['autor']
        #imagen = form.cleaned_data['imagen']
        #objetivo = form.cleaned_data['objetivo']
        estado = form.cleaned_data['estado']


        # Validar que el campo 'nombre' tenga al menos 3 caracteres
        if len(titulo) < 3:
            form.add_error ('titulo', "El titulo debe tener al menos 3 caracteres.")
            return self.form_invalid(form)
        
        if len(cuerpo) < 20:
            form.add_error ('cuerpo', "El cuerpo debe tener al menos 20 caracteres.")
            return self.form_invalid(form)
        
        if estado not in ['habilitado', 'deshabilitado']:  #controla que el estado sea solo 'habilitado', 'deshabilitado' 
            form.add_error('estado', "El estado debe ser 'habilitado' , 'deshabilitado'.")
            return self.form_invalid(form)
        
        messages.success(self.request, 'Noticia modificada exitosamente.')

        return super().form_valid(form) #Si el 'nombre' es válido, llamamos a super().form_valid(form) para guardar los cambios y redireccionar a la página de mostrar todas

    def get_form(self, form_class=None): #metodo que nos da un select para seleccionar habilitado o deshabilitado
        form = super().get_form(form_class) #metodo para obtener el formulario original generado por Django.
        form.fields['estado'].widget = forms.Select(choices=[('habilitado', 'Habilitado'), ('deshabilitado', 'Deshabilitado')]) # Asignamos el widget forms.Select al campo 'estado'
        return form
    

#delete
def eliminarNoticia(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk) #la funcion guarda en su variable pk el id de la noticia para luego borrarla
    noticia.delete()
    messages.success(request, 'Noticia eliminada exitosamente.')
    return redirect('noticias:listarNoticias')


def eliminarComentario(request, pk):
    comentario = get_object_or_404(Comentario, pk=pk) #la funcion guarda en su variable pk el id de la noticia para luego borrarla
    noticia_pk = comentario.noticia.pk  # Obtenemos el pk de la noticia asociada al comentario
    comentario.delete()
    messages.success(request, 'comentario eliminado exitosamente.')
    return redirect(reverse('noticias:mostrarNoticia', kwargs={'pk': noticia_pk}))

#__________________________________________________________________________________________

