# Generated by Django 3.2.4 on 2021-10-22 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0029_mesa_reserva'),
    ]

    operations = [
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
            name='Reserva',
        ),
    ]
