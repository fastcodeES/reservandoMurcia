# Generated by Django 3.2.4 on 2021-09-08 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0018_auto_20210908_2116'),
    ]

    operations = [
        migrations.AddField(
            model_name='mesa',
            name='personas',
            field=models.CharField(choices=[('EXTERIOR', 'EXTERIOR'), ('INTERIOR', 'INTERIOR')], default='4', max_length=20),
        ),
    ]
