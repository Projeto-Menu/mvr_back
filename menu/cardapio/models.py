# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cardapio(models.Model):
    id_cardapio = models.IntegerField(primary_key=True)
    tipo_refeicao = models.CharField(max_length=60, blank=True, null=True)
    hora_refeicao = models.CharField(max_length=255, blank=True, null=True)
    id_refeicoes = models.ForeignKey('Refeicoes', models.DO_NOTHING, db_column='id_refeicoes', blank=True, null=True)
    id_dia_funcionamento = models.ForeignKey('DiaFuncionamento', models.DO_NOTHING, db_column='id_dia_funcionamento', blank=True, null=True)

    class Meta:
        verbose_name = "Cardápio"
        verbose_name_plural = "Cardápios"
        managed = False
        db_table = 'cardapio'
        


class DiaFuncionamento(models.Model):
    id_dia_funcionamento = models.IntegerField(primary_key=True)
    dia_semana = models.CharField(max_length=60, blank=True, null=True)
    data_dia = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name = "Dia de Funcionamento"
        verbose_name_plural = "Dias de Funcionamento"
        managed = False
        db_table = 'dia_funcionamento'
        
    def __str__(self):
        data = str(self.data_dia)
        return data


class Feedback(models.Model):
    id_feedback = models.IntegerField(primary_key=True)
    nota_refeicao = models.IntegerField(blank=True, null=True)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario', blank=True, null=True)
    id_refeicao = models.ForeignKey('Refeicoes', models.DO_NOTHING, db_column='id_refeicao', blank=True, null=True)

    class Meta:
        verbose_name = "Feedback"
        verbose_name_plural = "Feedbacks"
        managed = False
        db_table = 'feedback'


class Refeicoes(models.Model):
    id_refeicoes = models.IntegerField(primary_key=True)
    nome_prato = models.CharField(max_length=60, blank=True, null=True)
    descricao = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = "Refeição"
        verbose_name_plural = "Refeições"
        managed = False
        db_table = 'refeicoes'
        
    def __str__(self):
        return self.nome_prato


class Usuario(models.Model):
    id_usuario = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=60, blank=True, null=True)
    email = models.CharField(max_length=60, blank=True, null=True)
    senha = models.CharField(max_length=60, blank=True, null=True)
    tipo_usuario = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    data_modificacao = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        managed = False
        db_table = 'usuario'
        
    def __str__(self):
        return self.nome
