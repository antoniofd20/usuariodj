# Generated by Django 3.0.6 on 2020-05-07 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='apellidos',
            field=models.CharField(blank=True, max_length=30, verbose_name='Apellidos'),
        ),
        migrations.AlterField(
            model_name='user',
            name='nombres',
            field=models.CharField(blank=True, max_length=30, verbose_name='Nombre(s)'),
        ),
    ]