# Generated by Django 3.2.4 on 2021-09-04 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0007_auto_20210904_1624'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='mesa',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='reservas.mesa'),
        ),
    ]
