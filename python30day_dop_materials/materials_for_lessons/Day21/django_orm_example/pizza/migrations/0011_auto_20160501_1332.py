# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-01 13:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0010_auto_20160501_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizzaorder',
            name='date_delivered',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]