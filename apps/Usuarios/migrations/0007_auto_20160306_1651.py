# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-07 00:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0006_remove_users_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]
