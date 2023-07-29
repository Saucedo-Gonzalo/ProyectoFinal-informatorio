from turtle import color
from django import forms 

from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
#La función gettext_lazy se utiliza para traducir cadenas de texto en aplicaciones de Django. Permite marcar las cadenas de texto para su traducción, de modo que puedan ser adaptadas a diferentes idiomas en el futuro.
from django.utils.translation import gettext_lazy as _
from .models import Usuario

#formato usual de registro de usuarios
class RegistroForm(UserCreationForm):
    Email = forms.EmailField(label='Email',required=True, 
                    widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    
    first_name = forms.CharField(label='Nombre',required=True, 
                    widget=forms.TextInput(attrs={'placeholder': 'Nombre'}))
    
    last_name = forms.CharField(label='Apellido', required=True, 
                    widget=forms.TextInput(attrs={'placeholder': 'Apellido'}))
    password1 = forms.CharField(
        label='Contraseña', widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(
        label='Confirmar Contraseña', widget=forms.PasswordInput, required=True)

    class Meta:
        model = Usuario
        fields = [
            'first_name',
            'last_name',
            'username',
            'Email',
            'password1',
            'password2',
        ]

# class CustomPasswordResetConfirmViewForm(PasswordResetForm):
#     error_messages = {
#         'password_mismatch': _('Las contraseñas no coinciden.'),
#     }