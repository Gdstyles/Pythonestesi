# Generated by Django 4.2.16 on 2024-11-20 23:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0002_fabrica_producto_fabrica'),
    ]

    operations = [
        migrations.AddField(
            model_name='fabrica',
            name='pais',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='producto',
            name='fecha_vencimiento',
            field=models.DateField(blank=True, default=datetime.datetime(2024, 11, 20, 20, 22, 28, 641864), null=True),
        ),
    ]
