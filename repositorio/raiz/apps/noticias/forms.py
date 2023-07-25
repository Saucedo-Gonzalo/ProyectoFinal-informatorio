from django import forms
from .models import Noticia


class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo', 'cuerpo', 'autor', 'imagen', 'objetivo', 'estado']

    def __init__(self, *args, **kwargs): #Al modificar el campo en el método __init__, aseguramos que se apliquen los cambios al formulario antes de que se renderice en la vista
        super().__init__(*args, **kwargs)
        self.fields['objetivo'].empty_label = 'Seleccione'
        self.fields['estado'].empty_label = 'Seleccione el estado'
        self.fields['estado'].choices = [('habilitado', 'Habilitado'), ('deshabilitado', 'Deshabilitado')]


