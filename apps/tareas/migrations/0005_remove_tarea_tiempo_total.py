# Generated by Django 3.0.4 on 2020-03-12 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0004_auto_20200312_1311'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tarea',
            name='tiempo_total',
        ),
    ]