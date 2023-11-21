from rest_framework import serializers
from .models import *

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id_usuario','nome','email','senha','tipo_usuario','status']
        
class RefeicoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Refeicoes
        fields = ['id_refeicoes','nome_prato','descricao']
        
class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['id_feedback','nota_refeicao','comentario','id_usuario','id_refeicao']
        
class DiaFuncionamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiaFuncionamento
        fields = ['id_dia_funcionamento','dia_semana','data_dia']

class CardapioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cardapio
        fields = ['id_cardapio','tipo_refeicao','hora_refeicao','id_refeicoes','id_dia_funcionamento']
