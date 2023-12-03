# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Cardapio(models.Model):
    id_cardapio = models.AutoField(primary_key=True)
    id_prato_principal = models.ForeignKey('Refeicoes', models.DO_NOTHING, db_column='id_prato_principal', blank=True, null=True)
    id_vegetariano = models.ForeignKey('Refeicoes', models.DO_NOTHING, db_column='id_vegetariano', related_name='cardapio_id_vegetariano_set', blank=True, null=True)
    id_guarnicao = models.ForeignKey('Refeicoes', models.DO_NOTHING, db_column='id_guarnicao', related_name='cardapio_id_guarnicao_set', blank=True, null=True)
    id_complemento = models.ForeignKey('Refeicoes', models.DO_NOTHING, db_column='id_complemento', related_name='cardapio_id_complemento_set', blank=True, null=True)
    id_salada_crua = models.ForeignKey('Refeicoes', models.DO_NOTHING, db_column='id_salada_crua', related_name='cardapio_id_salada_crua_set', blank=True, null=True)
    id_salada_cozida = models.ForeignKey('Refeicoes', models.DO_NOTHING, db_column='id_salada_cozida', related_name='cardapio_id_salada_cozida_set', blank=True, null=True)
    id_sobremesa = models.ForeignKey('Refeicoes', models.DO_NOTHING, db_column='id_sobremesa', related_name='cardapio_id_sobremesa_set', blank=True, null=True)
    id_bebida = models.ForeignKey('Refeicoes', models.DO_NOTHING, db_column='id_bebida', related_name='cardapio_id_bebida_set', blank=True, null=True)

    class Meta:
        verbose_name = "Cardápio"
        verbose_name_plural = "Cardápios"
        managed = False
        db_table = 'cardapio'


class DiaFuncionamento(models.Model):
    id_dia_funcionamento = models.AutoField(primary_key=True)
    id_almoco = models.ForeignKey(Cardapio, models.DO_NOTHING, db_column='id_almoco', blank=True, null=True)
    id_janta = models.ForeignKey(Cardapio, models.DO_NOTHING, db_column='id_janta', related_name='diafuncionamento_id_janta_set', blank=True, null=True)
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
    id_feedback = models.AutoField(primary_key=True)
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
    id_refeicoes = models.AutoField(primary_key=True)
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
    id_usuario = models.AutoField(primary_key=True)
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