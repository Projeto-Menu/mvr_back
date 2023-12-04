from django.urls import path, include
from menu.cardapio import views as v
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.generic import TemplateView


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
    path('api/register/', v.register_view, name='register-view'),
    path('api/login/', v.login_view, name='login-view'),
    path('api/logout/', v.logout_view, name='logout-view'),
    path('api/password-reset/', v.password_reset_view, name='password-reset-view'),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)