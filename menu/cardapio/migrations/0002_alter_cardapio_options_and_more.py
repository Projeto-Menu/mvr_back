# Generated by Django 4.2.7 on 2023-11-22 01:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cardapio', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cardapio',
            options={'managed': False, 'verbose_name': 'Cardápio', 'verbose_name_plural': 'Cardápios'},
        ),
        migrations.AlterModelOptions(
            name='diafuncionamento',
            options={'managed': False, 'verbose_name': 'Dia de Funcionamento', 'verbose_name_plural': 'Dias de Funcionamento'},
        ),
        migrations.AlterModelOptions(
            name='feedback',
            options={'managed': False, 'verbose_name': 'Feedback', 'verbose_name_plural': 'Feedbacks'},
        ),
        migrations.AlterModelOptions(
            name='refeicoes',
            options={'managed': False, 'verbose_name': 'Refeição', 'verbose_name_plural': 'Refeições'},
        ),
        migrations.AlterModelOptions(
            name='usuario',
            options={'managed': False, 'verbose_name': 'Usuário', 'verbose_name_plural': 'Usuários'},
        ),
    ]
