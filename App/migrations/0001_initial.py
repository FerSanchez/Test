# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-12 21:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=200)),
                ('Nacionalidad', models.CharField(blank=True, max_length=100, null=True)),
                ('Descripcion', models.TextField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Libros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=200)),
                ('Descripcion', models.TextField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='autores',
            name='libros',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='App.Libros'),
        ),
    ]
