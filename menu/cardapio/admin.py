from django.contrib import admin
from .models import *

# Register your models here.

class CardapioAdmin(admin.ModelAdmin):
  list_display = ("id_cardapio", "tipo_refeicao", "hora_refeicao","id_refeicoes","id_dia_funcionamento")
  
admin.site.register(Cardapio, CardapioAdmin)

class RefeicoesAdmin(admin.ModelAdmin):
  list_display = ("id_refeicoes", "nome_prato", "descricao")
  
admin.site.register(Refeicoes, RefeicoesAdmin)

class FeedbackAdmin(admin.ModelAdmin):
  list_display = ("id_feedback", "nota_refeicao", "comentario","id_usuario","id_refeicao")
  
admin.site.register(Feedback, FeedbackAdmin)

class UsuarioAdmin(admin.ModelAdmin):
  list_display = ("id_usuario", "nome", "email","senha","tipo_usuario","status","data_modificacao")
  
admin.site.register(Usuario, UsuarioAdmin)

class DiaFuncionamentoAdmin(admin.ModelAdmin):
  list_display = ("id_dia_funcionamento", "dia_semana", "data_dia",)
  
admin.site.register(DiaFuncionamento, DiaFuncionamentoAdmin)
