# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-12 02:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0010_auto_20160210_1321'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChartTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('size', models.CharField(max_length=2, verbose_name='size of your chart')),
                ('dataSetName', models.CharField(max_length=20, verbose_name='name of your array data')),
                ('status', models.BooleanField(default=1)),
                ('user', models.CharField(max_length=50)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('attribute', models.CharField(max_length=20, verbose_name='this is the name of the attribute')),
                ('dimensions', models.CharField(max_length=50, verbose_name='this is the names of the dimensions by coma seperated')),
                ('api', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.Api')),
                ('chartType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.ChartType')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='chart',
            name='api',
        ),
        migrations.RemoveField(
            model_name='chart',
            name='chartType',
        ),
        migrations.RemoveField(
            model_name='dashboard',
            name='chart',
        ),
        migrations.DeleteModel(
            name='Chart',
        ),
        migrations.AddField(
            model_name='dashboard',
            name='chart',
            field=models.ManyToManyField(to='apis.ChartTable'),
        ),
    ]
