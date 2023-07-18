from turtle import color
from django import forms 

from django.contrib.auth.forms import UserCreationForm
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