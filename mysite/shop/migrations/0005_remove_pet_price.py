# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-03 04:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_pet_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pet',
            name='price',
        ),
    ]
