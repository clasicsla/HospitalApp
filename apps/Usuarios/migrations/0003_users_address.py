# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-06 20:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0002_auto_20160306_0948'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='address',
            field=models.TextField(default='', verbose_name='Direccion'),
            preserve_default=False,
        ),
    ]
