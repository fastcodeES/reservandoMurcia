# Generated by Django 3.2.4 on 2021-09-09 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0020_auto_20210909_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mesa',
            name='lugar',
            field=models.CharField(choices=[('EXTERIOR', 'EXTERIOR'), ('INTERIOR', 'INTERIOR')], max_length=20, null=True),
        ),
    ]
