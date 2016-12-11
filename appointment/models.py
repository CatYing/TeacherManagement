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


# 老师的时间段
class TeacherPeriod(models.Model):
    date = models.DateField(blank=True, null=True)
    time_period = models.ForeignKey(TimePeriod)
    teacher = models.ForeignKey(MyUser)
    free = models.BooleanField()

    def __unicode__(self):
        return unicode(self.date) + u'的第' + self.time_period.name + u'节'


class TeacherEnroll(models.Model):
    teacher = models.OneToOneField(MyUser)

    def __unicode__(self):
        return self.teacher.name


# 预约对象
class AppointmentObject(models.Model):
    student = models.ForeignKey(MyUser)
    teacher_enroll = models.ForeignKey(TeacherEnroll)
    teacher_period = models.ForeignKey(TeacherPeriod)
    result = models.IntegerField(default=-1)

    def __unicode__(self):
        return self.student.name + u'对' + self.teacher_enroll.teacher.name + u'预约'
