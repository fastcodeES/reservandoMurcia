# Generated by Django 3.2.4 on 2021-09-06 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0014_alter_evento_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='imagen',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
