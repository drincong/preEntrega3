# Generated by Django 5.0.6 on 2024-06-14 02:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppPreEntrega3', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='oferta',
            name='tienda_donde_aplica',
        ),
    ]
