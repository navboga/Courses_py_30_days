# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-08 15:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0006_auto_20160508_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theme',
            name='name',
            field=models.CharField(max_length=35),
        ),
    ]