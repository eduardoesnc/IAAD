# Generated by Django 4.2 on 2023-04-14 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('CodMed', models.CharField(max_length=7,auto_created=True, primary_key=True, serialize=False, verbose_name='CodMed')),
                ('NomeMed', models.CharField(max_length=40)),
                ('Genero', models.CharField(max_length=1)),
                ('Telefone', models.CharField(max_length=16)),
                ('Email', models.CharField(max_length=40)),
                ('CodEspec', models.CharField(max_length=7)),
            ],
        ),
    ]
