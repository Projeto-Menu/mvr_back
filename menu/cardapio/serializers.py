from rest_framework import serializers
from .models import *

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id','username','email']
        
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
        fields = ['id_dia_funcionamento','id_almoco','id_janta','dia_semana','data_dia']

class CardapioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cardapio
        fields = ['id_cardapio',"id_prato_principal","id_vegetariano","id_guarnicao","id_complemento","id_salada_crua","id_salada_cozida","id_sobremesa","id_bebida"]
