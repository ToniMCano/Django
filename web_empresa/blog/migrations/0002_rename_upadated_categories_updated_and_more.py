# Generated by Django 5.0.6 on 2024-07-03 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categories',
            old_name='upadated',
            new_name='updated',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='upadated',
            new_name='updated',
        ),
    ]
