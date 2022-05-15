# Generated by Django 3.2.4 on 2021-09-02 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('nombre', models.CharField(max_length=60, primary_key=True, serialize=False)),
                ('descripcion', models.TextField(max_length=300)),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Plato',
        ),
    ]
