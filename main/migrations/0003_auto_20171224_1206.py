# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-24 04:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20171223_1828'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='info',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='entity',
            name='info',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='genus',
            name='info',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='stage',
            name='info',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='tag',
            name='info',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
