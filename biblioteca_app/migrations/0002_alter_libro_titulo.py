# Generated by Django 3.2.6 on 2023-09-07 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='titulo',
            field=models.CharField(max_length=50, verbose_name='Nombre'),
        ),
    ]
