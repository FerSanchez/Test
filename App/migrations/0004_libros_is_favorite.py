# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-14 22:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_libros_portada'),
    ]

    operations = [
        migrations.AddField(
            model_name='libros',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
    ]
