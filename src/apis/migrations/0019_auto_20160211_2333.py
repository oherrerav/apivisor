# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-12 04:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0018_auto_20160211_2325'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dashboard',
            old_name='chart',
            new_name='charts',
        ),
    ]
