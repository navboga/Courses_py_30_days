# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-23 17:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0004_auto_20160422_1816'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AvaliablePizzaSizes',
            new_name='SizeOptions',
        ),
    ]
