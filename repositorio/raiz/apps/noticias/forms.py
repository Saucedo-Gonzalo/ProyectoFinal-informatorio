from django import forms
from .models import Noticia, Objetivo


class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo', 'cuerpo', 'autor', 'imagen', 'objetivo']

    def __init__(self, *args, **kwargs): #Al modificar el campo en el método __init__, aseguramos que se apliquen los cambios al formulario antes de que se renderice en la vista
        super().__init__(*args, **kwargs)
        self.fields['objetivo'].empty_label = 'Seleccione'


