# Generated by Django 3.2.4 on 2021-10-22 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contactos', '0003_alter_contacto_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contacto',
            name='avisos',
        ),
    ]
