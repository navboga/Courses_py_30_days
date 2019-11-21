# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-01 10:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0007_auto_20160501_1012'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pizzasize',
            options={'ordering': ['size']},
        ),
        migrations.AddField(
            model_name='pizzasize',
            name='full_name',
            field=models.CharField(default='', max_length=25),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pizzasize',
            name='size',
            field=models.CharField(max_length=5),
        ),
        migrations.DeleteModel(
            name='SizeOption',
        ),
    ]