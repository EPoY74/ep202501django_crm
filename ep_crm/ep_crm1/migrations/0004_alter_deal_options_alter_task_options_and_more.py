# Generated by Django 5.1.5 on 2025-01-23 05:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ep_crm1', '0003_alter_client_options_alter_client_address_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='deal',
            options={'verbose_name': 'Сделка', 'verbose_name_plural': 'Сделки'},
        ),
        migrations.AlterModelOptions(
            name='task',
            options={'verbose_name': 'Задача', 'verbose_name_plural': 'Задачи'},
        ),
        migrations.AlterField(
            model_name='deal',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Сумма'),
        ),
        migrations.AlterField(
            model_name='deal',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ep_crm1.client', verbose_name='Клиент'),
        ),
        migrations.AlterField(
            model_name='deal',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='deal',
            name='status',
            field=models.CharField(max_length=50, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='task',
            name='completed',
            field=models.BooleanField(default=False, verbose_name='Исполнено'),
        ),
        migrations.AlterField(
            model_name='task',
            name='deal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ep_crm1.deal', verbose_name='Сделка'),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_time',
            field=models.DateTimeField(verbose_name='Исполнить до'),
        ),
    ]