# Generated by Django 3.2.4 on 2021-11-27 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0051_alter_reserva_horario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='horario',
            field=models.IntegerField(choices=[[15, '15:00'], [19, '19:00']]),
        ),
    ]
