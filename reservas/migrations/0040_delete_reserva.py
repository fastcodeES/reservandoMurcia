# Generated by Django 3.2.4 on 2021-10-27 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0039_rename_username_reserva_nombre_usuario'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Reserva',
        ),
    ]
