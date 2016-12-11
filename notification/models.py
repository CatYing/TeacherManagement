# coding=utf8
from __future__ import unicode_literals

from django.db import models
from authentication.models import *

# Create your models here.


class StudentNotificationsOnTeacher(models.Model):
    myuser = models.OneToOneField(MyUser)
    unread_count = models.IntegerField(default=0)

    def __unicode__(self):
        return self.myuser.name + u'的未读教师更新为' + unicode(self.unread_count)


class StudentNotificationOnAppointment(models.Model):
    myuser = models.OneToOneField(MyUser)
    unread_count = models.IntegerField(default=0)

    def __unicode__(self):
        return self.myuser.name + u'的未读预约更新为' + unicode(self.unread_count)



