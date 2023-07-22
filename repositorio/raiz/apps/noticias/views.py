#VER QUE NO SIRVE
from django import forms
from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import UpdateView, DeleteView, CreateView
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import NoticiaForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib import messages

from .models import Noticia,Comentario

#vistas CRUD
#create
def agregarNoticia(request):
    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES)
        if form.is_valid():
            noticia = form.save(commit=False)  # No guardar aún la instancia de Noticia en la base de datos
            noticia.autor = request.user  # Asignar el usuario actual como autor de la noticia
            noticia.save()  # Ahora sí guardamos la instancia de Noticia con el autor asignado
            messages.success(request, 'Noticia modificada exitosamente.')
            return redirect('noticias:listarNoticias')
    else:
        form = NoticiaForm()
    return render(request, 'noticias/agregarNoticia.html', {'form': form})

#read
def listarNoticias(request):
    noticias = Noticia.objects.all()   # Muestra todas las noticias
    context = {'noticias': noticias}
    return render(request, 'noticias/listarNoticias.html', context)

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
    noticia = get_object_or_404(Noticia, pk=pk) #la funcion guarda en su variable pk el id de la universidad para luego borrarla
    noticia.delete()
    messages.success(request, 'Noticia eliminada exitosamente.')
    return redirect('noticias:listarNoticias')
