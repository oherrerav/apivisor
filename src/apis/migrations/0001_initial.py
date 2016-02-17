# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-16 03:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Api',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('uri', models.CharField(max_length=500)),
                ('user', models.CharField(max_length=50)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Chart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('size', models.CharField(choices=[('1', '1x'), ('2', '2x'), ('3', '3x')], help_text='size of your chart', max_length=2)),
                ('dataSet', models.CharField(max_length=20)),
                ('attribute', models.CharField(max_length=20)),
                ('dimensions', models.CharField(max_length=100)),
                ('options', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=1)),
                ('user', models.CharField(max_length=50)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('api', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.Api')),
            ],
        ),
        migrations.CreateModel(
            name='ChartType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('status', models.BooleanField(default=1)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ChartVisualization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('status', models.BooleanField(default=1)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='DashBoard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('default', models.BooleanField()),
                ('status', models.BooleanField(default=1)),
                ('user', models.CharField(max_length=50)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('charts', models.ManyToManyField(to='apis.Chart')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='EventDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_date', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='event_dates',
            field=models.ManyToManyField(to='apis.EventDate'),
        ),
        migrations.AddField(
            model_name='charttype',
            name='chartVisualization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.ChartVisualization'),
        ),
        migrations.AddField(
            model_name='chart',
            name='chartType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.ChartType'),
        ),
    ]
