# Generated by Django 2.1.5 on 2020-03-25 05:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('incidencias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Incidencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, max_length=40)),
                ('estatus', models.CharField(choices=[('Por Revisar', 'Por Revisar'), ('Revisado', 'Revisado'), ('Resuelto', 'Resuelto'), ('Descartada', 'Descartada')], default='Por Revisar', max_length=40)),
                ('tipo', models.CharField(choices=[('Retraso', 'Retraso'), ('Error', 'Error'), ('Ausencia', 'Ausencia'), ('Problema Tecnico', 'Problema Tecnico'), ('Otro', 'Otro')], default='Retraso', max_length=40)),
                ('descripcion', models.CharField(blank=True, max_length=200)),
                ('fecha_reporte', models.DateField(auto_now_add=True)),
                ('fecha_reportada', models.DateField()),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='incidencias',
            name='usuario',
        ),
        migrations.DeleteModel(
            name='Incidencias',
        ),
    ]
