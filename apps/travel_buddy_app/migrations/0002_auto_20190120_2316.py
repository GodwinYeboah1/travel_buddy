# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-01-20 23:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel_buddy_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='travel_date_from',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='trip',
            name='travel_date_to',
            field=models.CharField(max_length=100),
        ),
    ]
