# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-07 21:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0011_auto_20160307_1055'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='phone',
        ),
    ]
