from django.urls import path
from menu.cardapio import views as v
from rest_framework.urlpatterns import format_suffix_patterns


app_name = 'menu.cardapio'


urlpatterns = [
    path('api/usuarios/<int:pk>/', v.usuario_detail),
    path('api/usuarios/', v.usuario_list, name='usuarios'),
    path('api/refeicoes/<int:pk>/', v.refeicoes_detail),
    path('api/refeicoes/', v.refeicoes_list, name='refeicoes'),
    path('api/feedback/<int:pk>/', v.feedback_detail),
    path('api/feedback/', v.feedback_list, name='feedback'),
    path('api/diaFuncionamento/<int:pk>/', v.diaFuncionamento_detail),
    path('api/diaFuncionamento/', v.diaFuncionamento_list, name='diaFuncionamento'),
    path('api/cardapio/<int:pk>/', v.cardapio_detail),
    path('api/cardapio/', v.cardapio_list, name='cardapio'),

]

urlpatterns = format_suffix_patterns(urlpatterns)