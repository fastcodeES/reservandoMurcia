# Generated by Django 3.2.4 on 2021-11-14 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='completado',
            field=models.IntegerField(choices=[[0, 'SI'], [1, 'NO']]),
        ),
    ]
