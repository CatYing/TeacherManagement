# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-11 19:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0002_auto_20161210_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointmentobject',
            name='result',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
