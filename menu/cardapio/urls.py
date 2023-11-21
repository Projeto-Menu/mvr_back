from django.urls import path
from menu.cardapio import views as v


app_name = 'menu.cardapio'


urlpatterns = [
    path('api/usuarios/', v.api_usuarios, name='usuarios'),
    path('api/refeicoes/', v.api_refeicoes, name='refeicoes'),
    path('api/diaFuncionamento/', v.api_diaFuncionamento, name='diaFuncionamento'),
    path('api/feedback/', v.api_feedback, name='feedback'),
    path('api/cardapio/', v.api_cardapio, name='cardapio'),
]