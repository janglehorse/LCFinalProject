# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-18 16:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mealplanner', '0002_auto_20170417_1545'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShoppingList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.AlterModelOptions(
            name='ingredient',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='instruction',
            options={'ordering': ('number',)},
        ),
        migrations.AlterModelOptions(
            name='recipe',
            options={'ordering': ('name',)},
        ),
        migrations.AddField(
            model_name='shoppinglist',
            name='recipes',
            field=models.ManyToManyField(to='mealplanner.Recipe'),
        ),
    ]
