# Generated by Django 3.2.12 on 2022-03-04 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_opciones_opciones_perfil'),
    ]

    operations = [
        migrations.AddField(
            model_name='opciones',
            name='url',
            field=models.CharField(default='', max_length=100),
        ),
    ]
