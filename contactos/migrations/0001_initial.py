# Generated by Django 3.2.4 on 2021-10-10 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=254)),
                ('tipo_consultas', models.IntegerField(choices=[[0, 'consulta'], [1, 'reclamo'], [3, 'sugerencia']])),
                ('mensaje', models.TextField(max_length=3000)),
                ('avisos', models.BooleanField()),
            ],
        ),
    ]
