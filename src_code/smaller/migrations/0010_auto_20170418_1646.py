# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-04-18 16:46
from __future__ import unicode_literals

from django.db import migrations, models
import smaller.forms


class Migration(migrations.Migration):

    dependencies = [
        ('smaller', '0009_auto_20170412_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smallurl',
            name='url',
            field=models.CharField(default=None, max_length=220, validators=[smaller.forms.validate_url, smaller.forms.validate_www]),
        ),
    ]
