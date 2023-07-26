from django import forms
from .models import Noticia



class NoticiaAgregarForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo', 'cuerpo', 'autor', 'imagen', 'objetivo', 'estado']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['objetivo'].empty_label = 'Seleccione'
        # No mostraremos el campo 'estado' en el formulario
        self.fields['estado'].widget = forms.HiddenInput()
        self.fields['estado'].initial = 'habilitado'  # O el valor que desees
        self.fields['autor'].widget = forms.HiddenInput()
        

    def clean_titulo(self):
        titulo = self.cleaned_data.get('titulo')
        if len(titulo) < 3:
            raise forms.ValidationError("El título debe tener al menos 3 caracteres.")
        return titulo

    def clean_cuerpo(self):
        cuerpo = self.cleaned_data.get('cuerpo')
        if len(cuerpo) < 20:
            raise forms.ValidationError("El cuerpo debe tener al menos 20 caracteres.")
        return cuerpo
    

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo', 'cuerpo', 'autor', 'imagen', 'objetivo', 'estado']


    def __init__(self, *args, **kwargs): #Al modificar el campo en el método __init__, aseguramos que se apliquen los cambios al formulario antes de que se renderice en la vista
        super().__init__(*args, **kwargs)
        self.fields['objetivo'].empty_label = 'Seleccione'
        self.fields['estado'].empty_label = 'Seleccione el estado'
        self.fields['estado'].choices = [('habilitado', 'Habilitado'), ('deshabilitado', 'Deshabilitado')]


