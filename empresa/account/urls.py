from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('perfil/', editar_perfil, name='editar_perfil'),
    path('cambiar-password/', cambiar_password, name='password_change'),
    path('password-ok/', password_change_done, name='password_change_done'),
]