# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-17 00:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0004_auto_20160216_1941'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='event_dates',
        ),
        migrations.DeleteModel(
            name='Event',
        ),
        migrations.DeleteModel(
            name='EventDate',
        ),
    ]
