# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-03 18:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_delete_pet'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Products',
            new_name='Pet',
        ),
    ]
