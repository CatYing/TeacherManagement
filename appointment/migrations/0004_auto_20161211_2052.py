# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-11 20:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0003_auto_20161211_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointmentobject',
            name='result',
            field=models.IntegerField(default=-1),
        ),
    ]
