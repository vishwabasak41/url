# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-04-12 18:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smaller', '0008_auto_20170411_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smallurl',
            name='newurl',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
    ]
