# Generated by Django 3.2.4 on 2021-09-06 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0010_mesa_reserva'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=30)),
                ('imagen', models.ImageField(upload_to='reservas/images')),
            ],
        ),
    ]
