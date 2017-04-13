# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-12 22:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mealplanner', '0008_auto_20170412_2242'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=4)),
                ('unitOfMeasure', models.CharField(choices=[('CP', 'Cup'), ('TB', 'tbs'), ('TS', 'tsp'), ('LB', 'lb'), ('OZ', 'oz'), ('FO', 'fl oz'), ('NA', 'none')], default='CP', max_length=2)),
            ],
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='unitOfMeasure',
        ),
        migrations.AddField(
            model_name='ingredient',
            name='unit',
            field=models.ManyToManyField(to='mealplanner.Unit'),
        ),
    ]
