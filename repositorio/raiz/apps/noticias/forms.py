from django import forms
from .models import Noticia, Objetivo


class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo', 'cuerpo', 'autor', 'imagen', 'objetivo']




