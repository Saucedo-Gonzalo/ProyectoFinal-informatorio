from django.urls import path
from . import views

from django.contrib.auth import views as auth

app_name= 'usuarios'

urlpatterns = [
    
    path('registrarse/',views.registrarse.as_view(), name='registrarse'),
    path('login/',auth.LoginView.as_view(template_name='usuarios/loguearse.html'),name='loguearse'), #en vez de pasarle una vista mia paso una de django
    path('logout/',auth.LogoutView.as_view(),name="logout"),
    
]