# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-19 13:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('performance_collection', '0010_auto_20180219_0650'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='score',
            name='author',
        ),
        migrations.AddField(
            model_name='score',
            name='author',
            field=models.ManyToManyField(to='performance_collection.Name'),
        ),
    ]
