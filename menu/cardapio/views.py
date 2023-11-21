from .models import *
from django.http import JsonResponse


def api_usuarios(request):
    usuarios = Usuario.objects.all()
    data = []
    for user in usuarios:
        userdata = [{'id':user.id_usuario},{'nome':user.nome},{'email':user.email},{'senha':user.senha},
                    {'tipo':user.tipo_usuario},{'status':user.status},{'data modificacao':user.data_modificacao}]
        data.append(userdata)
    response = {'Dados de Usuarios': data}
    return JsonResponse(response)

def api_refeicoes(request):
    refeicoes = Refeicoes.objects.all()
    data = []
    for refeicao in refeicoes:
        itemdata = [{'id':refeicao.id_refeicoes},{'nome':refeicao.nome_prato},{'descricao':refeicao.descricao}]
        data.append(itemdata)
    response = {'Dados de refeicoes': data}
    return JsonResponse(response)

def api_feedback(request):
    feedback = Feedback.objects.all()
    data = []
    for item in feedback:
        itemdata = [{'id':item.id_feedback},{'nota':item.nota_refeicao},{'comentario':item.comentario},{'id_usuario':item.id_usuario.id_usuario},{'id_refeicao':item.id_refeicao.id_refeicoes}]
        data.append(itemdata)
    response = {'Dados de feedback': data}
    return JsonResponse(response)

def api_diaFuncionamento(request):
    diaFuncionamento = DiaFuncionamento.objects.all()
    data = []
    for item in diaFuncionamento:
        itemdata = [{'id':item.id_dia_funcionamento},{'dia_semana':item.dia_semana},{'data_dia':item.data_dia}]
        data.append(itemdata)
    response = {'Dados de diaFuncionamento': data}
    return JsonResponse(response)

def api_cardapio(request):
    cardapio = Cardapio.objects.all()
    data = []
    for item in cardapio:
        itemdata = [{'id':item.id_cardapio},{'tipo_refeicao':item.tipo_refeicao},{'hora_refeicao':item.hora_refeicao},{'id_refeicoes':item.id_refeicoes.id_refeicoes},{'id_dia_funcionamento':item.id_dia_funcionamento.id_dia_funcionamento}]
        data.append(itemdata)
    response = {'Dados de cardapio': data}
    return JsonResponse(response)