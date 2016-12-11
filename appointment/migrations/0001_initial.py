# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-10 13:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppointmentObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.BooleanField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.MyUser')),
            ],
        ),
        migrations.CreateModel(
            name='TeacherEnroll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='authentication.MyUser')),
            ],
        ),
        migrations.CreateModel(
            name='TeacherPeriod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('free', models.BooleanField()),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.MyUser')),
            ],
        ),
        migrations.CreateModel(
            name='TimePeriod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='teacherperiod',
            name='time_period',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointment.TimePeriod'),
        ),
        migrations.AddField(
            model_name='appointmentobject',
            name='teacher_enroll',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointment.TeacherEnroll'),
        ),
        migrations.AddField(
            model_name='appointmentobject',
            name='teacher_period',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointment.TeacherPeriod'),
        ),
    ]