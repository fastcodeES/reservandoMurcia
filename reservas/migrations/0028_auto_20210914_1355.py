# Generated by Django 3.2.4 on 2021-09-14 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0027_delete_evento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mesasdisponibles',
            name='mesa',
        ),
        migrations.RemoveField(
            model_name='reserva',
            name='mesa',
        ),
        migrations.RemoveField(
            model_name='reserva',
            name='usuario',
        ),
        migrations.DeleteModel(
            name='Mesa',
        ),
        migrations.DeleteModel(
            name='MesasDisponibles',
        ),
        migrations.DeleteModel(
            name='Reserva',
        ),
    ]
