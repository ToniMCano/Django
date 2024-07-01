# Generated by Django 5.0.6 on 2024-07-01 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='services',
            options={'ordering': ['-created'], 'verbose_name': 'Servicio', 'verbose_name_plural': 'Servicios'},
        ),
        migrations.AlterField(
            model_name='services',
            name='created',
            field=models.DateField(auto_now_add=True, verbose_name='Fecha de Creación'),
        ),
        migrations.AlterField(
            model_name='services',
            name='updated',
            field=models.DateField(auto_now=True, verbose_name='Fecha de Actualización'),
        ),
    ]
