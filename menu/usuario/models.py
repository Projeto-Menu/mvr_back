from django.db import models

# Create your models here.

class Usuario(models.Model):
    nome = models.CharField('Nome', max_length=20)
    sobrenome = models.CharField('Sobrenome', max_length=100)
    email = models.EmailField('E-mail',unique=True)
    senha = models.CharField('Senha', max_length=20)
    
    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        ordering = ['nome']
        