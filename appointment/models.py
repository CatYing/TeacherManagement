# coding=utf8
from __future__ import unicode_literals
from django.db import models
from authentication.models import MyUser

# Create your models here.


# 时间段（1-2节等）
class TimePeriod(models.Model):
    name = models.CharField(max_length=32)

    def __unicode__(self):
        return self.name


# 星期*
class Day(models.Model):
    name = models.CharField(max_length=32)

    def __unicode__(self):
        return self.name


# 周数
class Week(models.Model):
    name = models.CharField(max_length=32)

    def __unicode__(self):
        return u'第 %s' % self.name + u'周'


# 老师的时间段
class TeacherPeriod(models.Model):
    week = models.ForeignKey(Week)
    day = models.ForeignKey(Day)
    time_period = models.ForeignKey(TimePeriod)
    teacher = models.ForeignKey(MyUser)
    free = models.BooleanField()

    def __unicode__(self):
        return self.week + u'的' + self.day + u'的' + self.time_period

