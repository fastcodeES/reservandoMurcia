# Generated by Django 3.2.4 on 2021-09-09 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0023_alter_mesa_personas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mesa',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
    ]