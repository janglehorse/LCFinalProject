# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-09 01:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mealplanner', '0002_remove_recipe_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.CharField(max_length=750, null=True),
        ),
    ]
