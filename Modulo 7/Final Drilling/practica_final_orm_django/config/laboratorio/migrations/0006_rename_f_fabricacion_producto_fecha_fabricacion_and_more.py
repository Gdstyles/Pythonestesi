# Generated by Django 4.2.16 on 2024-12-07 00:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorio', '0005_actualizado_campos'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='f_fabricacion',
            new_name='fecha_fabricacion',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='p_costo',
            new_name='precio_costo',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='p_venta',
            new_name='precio_venta',
        ),
    ]