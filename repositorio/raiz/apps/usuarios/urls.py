from django.urls import path, reverse_lazy
from . import views

from django.contrib.auth import views as auth

app_name= 'usuarios'


urlpatterns = [
    
    path('registrarse/',views.registrarse.as_view(), name='registrarse'),
    path('login/',auth.LoginView.as_view(template_name='usuarios/loguearse.html'),name='loguearse'), #en vez de pasarle una vista mia paso una de django
    path('logout/',auth.LogoutView.as_view(),name="logout"),
    path('listar/',views.listarUsuarios,name="listarUsuarios"),
    path('eliminar/<int:pk>',views.eliminarUsuario,name="eliminarUsuario"),    
    path('modificar/<int:pk>',views.modificarUsuario,name="modificarUsuario"),   
    
    #modificar Password
    path('password_change/', views.password_change.as_view(), name='password_change'),
    path('password_success/', views.password_success, name='password_success'),
    #recuperacion de Password
    path(
        'password_reset/',
        auth.PasswordResetView.as_view(
        template_name='usuarios/reestablecerPassword/password_reset_form.html',
        email_template_name='usuarios/reestablecerPassword/password_reset_email.html',
        success_url=reverse_lazy('usuarios:password_reset_done')),
        name='password_reset'),
    path(
        'password_reset_done/',
        auth.PasswordResetDoneView.as_view(
        template_name='usuarios/reestablecerPassword/password_reset_done.html'),
        name='password_reset_done'),

    path(
        'password_reset/<uidb64>/<token>',
        auth.PasswordResetConfirmView.as_view(
        template_name='usuarios/reestablecerPassword/password_reset_confirm.html',
        success_url=reverse_lazy('usuarios:password_reset_complete')),
        name='password_reset_confirm'),

    path('password_reset_complete/',
        views.CustomPasswordResetCompleteView.as_view(
        template_name='usuarios/reestablecerPassword/password_reset_complete.html'),
        name='password_reset_complete'),                                
]