from django.urls import path

from .views import CriaUsuario


urlpatterns = [
    path('cadastro', CriaUsuario.as_view(), name = 'cadastro' )
]