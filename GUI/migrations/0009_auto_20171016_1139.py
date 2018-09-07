# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-16 11:39
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('GUI', '0008_auto_20170922_1247'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='pub_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='defense_node',
            name='date_added',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]