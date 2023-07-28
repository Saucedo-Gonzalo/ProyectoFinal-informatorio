from django.urls import path, reverse_lazy
from . import views

from django.contrib.auth import views as auth

app_name= 'usuarios'

urlpatterns = [
    
    path('registrarse/',views.registrarse.as_view(), name='registrarse'),
    #recuperacion de Password
    # path(
    #     'password_reset/',
    #     auth.PasswordResetView.as_view(
    #     template_name='usuarios/reestablecerPassword/password_reset.html',
    #     success_url=reverse_lazy('usuarios:password_reset_done')),
    #     #email_template_name='usuarios/reestablecerPassword/password_reset_email.html',
    #     name='password_reset'),
    # path(
    #     'password_reset_done/',
    #     auth.PasswordResetDoneView.as_view(
    #     template_name='usuarios/reestablecerPassword/password_reset_done.html'),
    #     name='password_reset_done'),

    # path(
    #     'password_reset/<uidb64>/<token>',
    #     auth.PasswordResetConfirmView.as_view(
    #     template_name='usuarios/reestablecerPassword/password_reset_confirm.html',
    #     success_url=reverse_lazy('usuarios:password_reset_complete')),
    #     name='password_reset_confirm'),

    # path('password_reset_complete/',
    #      auth.PasswordResetCompleteView.as_view(
    #     template_name='usuarios/reestablecerPassword/password_reset_complete.html'),
    #     name='password_reset_complete'),                                

    path('password_reset/', auth.PasswordResetView.as_view(template_name='usuarios/reestablecerPassword/password_reset_form.html', email_template_name='usuarios/reestablecerPassword/password_reset_email.html'), name='password_reset'),
    path('password_reset/done/', auth.PasswordResetDoneView.as_view(template_name='usuarios/reestablecerPassword/password_reset_done.html'), name='password_reset_done'),
    path('reset/<str:uidb64>/<str:token>/', auth.PasswordResetConfirmView.as_view(template_name='usuarios/reestablecerPassword/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth.PasswordResetCompleteView.as_view(template_name='usuarios/reestablecerPassword/password_reset_complete.html'), name='password_reset_complete'),

    path('login/',auth.LoginView.as_view(template_name='usuarios/loguearse.html'),name='loguearse'), #en vez de pasarle una vista mia paso una de django
    path('logout/',auth.LogoutView.as_view(),name="logout"),

]