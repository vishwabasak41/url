# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-04-11 15:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smaller', '0006_auto_20170411_1528'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='smallurl',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='smallurl',
            name='newurl',
            field=models.CharField(blank=True, default='', max_length=25, null=True, unique=True),
        ),
    ]
