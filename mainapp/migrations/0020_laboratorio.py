# Generated by Django 3.2.12 on 2022-03-20 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0019_consulta'),
    ]

    operations = [
        migrations.CreateModel(
            name='Laboratorio',
            fields=[
                ('id_estudioLaboratotio', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('id_consulta', models.IntegerField(null=True)),
                ('idpaciente', models.IntegerField(null=True)),
                ('iddoctor', models.IntegerField(null=True)),
                ('id_estudio', models.IntegerField(null=True)),
                ('notas_recomendaciones', models.CharField(default='', max_length=250)),
                ('fecha', models.DateField(null=True)),
                ('estado', models.IntegerField(default=1)),
            ],
        ),
    ]