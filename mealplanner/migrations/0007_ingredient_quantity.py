# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-12 17:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mealplanner', '0006_auto_20170412_1707'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]