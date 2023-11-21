from .models import *
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *


@api_view(['GET', 'POST'])
def usuario_list(request,format=None):
    """
    Lista ou cria usuários
    """
    
    if request.method == 'GET':
        usuario = Usuario.objects.all()
        serializer = UsuarioSerializer(usuario, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def usuario_detail(request, pk, format=None):
    """
    Visualizar, atualizar ou deletar um usuário.
    """
    try:
        usuario = Usuario.objects.get(pk=pk)
    except usuario.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = UsuarioSerializer(usuario)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UsuarioSerializer(usuario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def cardapio_list(request,format=None):
    """
    Lista ou cria usuários
    """
    
    if request.method == 'GET':
        cardapio = Cardapio.objects.all()
        serializer = CardapioSerializer(cardapio, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CardapioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def cardapio_detail(request, pk, format=None):
    """
    Visualizar, atualizar ou deletar um usuário.
    """
    try:
        cardapio = Cardapio.objects.get(pk=pk)
    except cardapio.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = CardapioSerializer(cardapio)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CardapioSerializer(cardapio, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        cardapio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def refeicoes_list(request,format=None):
    """
    Lista ou cria usuários
    """
    
    if request.method == 'GET':
        refeicoes = Refeicoes.objects.all()
        serializer = RefeicoesSerializer(refeicoes, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RefeicoesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def refeicoes_detail(request, pk, format=None):
    """
    Visualizar, atualizar ou deletar um usuário.
    """
    try:
        refeicoes = Refeicoes.objects.get(pk=pk)
    except refeicoes.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = RefeicoesSerializer(refeicoes)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = RefeicoesSerializer(refeicoes, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        refeicoes.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def feedback_list(request,format=None):
    """
    Lista ou cria usuários
    """
    
    if request.method == 'GET':
        feedback = Feedback.objects.all()
        serializer = FeedbackSerializer(feedback, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = FeedbackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def feedback_detail(request, pk, format=None):
    """
    Visualizar, atualizar ou deletar um usuário.
    """
    try:
        feedback = feedback.objects.get(pk=pk)
    except feedback.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = FeedbackSerializer(feedback)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = FeedbackSerializer(feedback, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        feedback.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def diaFuncionamento_list(request,format=None):
    """
    Lista ou cria usuários
    """
    
    if request.method == 'GET':
        diaFuncionamento = diaFuncionamento.objects.all()
        serializer = DiaFuncionamentoSerializer(diaFuncionamento, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DiaFuncionamentoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def diaFuncionamento_detail(request, pk, format=None):
    """
    Visualizar, atualizar ou deletar um usuário.
    """
    try:
        diaFuncionamento = DiaFuncionamento.objects.get(pk=pk)
    except diaFuncionamento.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = DiaFuncionamentoSerializer(diaFuncionamento)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DiaFuncionamentoSerializer(diaFuncionamento, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        diaFuncionamento.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
