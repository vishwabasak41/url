# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-04-20 16:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('smaller', '0010_auto_20170418_1646'),
    ]

    operations = [
        migrations.CreateModel(
            name='clicks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('small_url', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='smaller.smallurl')),
            ],
            managers=[
                ('objec', django.db.models.manager.Manager()),
            ],
        ),
    ]