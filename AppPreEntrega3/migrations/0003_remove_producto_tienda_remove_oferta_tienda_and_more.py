# Generated by Django 5.0.6 on 2024-06-14 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppPreEntrega3', '0002_remove_oferta_tienda_donde_aplica'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='tienda',
        ),
        migrations.RemoveField(
            model_name='oferta',
            name='tienda',
        ),
        migrations.AddField(
            model_name='oferta',
            name='tienda',
            field=models.ManyToManyField(to='AppPreEntrega3.tienda'),
        ),
    ]