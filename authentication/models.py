# coding=utf8
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# identity代表身份，1为学生，2为教师
class MyUser(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=64)
    identity = models.IntegerField(default=1)

    def __unicode__(self):
        return self.name


# 学生信息
class StudentInfo(models.Model):
    student_id = models.CharField(max_length=16, blank=True)
    e_mail = models.EmailField(blank=True)
    cellphone = models.CharField(max_length=64, blank=True)
    cell_private = models.BooleanField(default=False, blank=True)
    college = models.CharField(max_length=64, blank=True)
    grade = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True)
    myuser = models.OneToOneField(MyUser)

    def __unicode__(self):
        return self.myuser.name + u"学生信息"


# 教师信息
class TeacherInfo(models.Model):
    teacher_id = models.CharField(max_length=16)
    e_mail = models.EmailField()
    cellphone = models.CharField(max_length=64, blank=True)
    cell_private = models.BooleanField(default=False)
    address = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    myuser = models.OneToOneField(MyUser)

    def __unicode__(self):
        return self.myuser.name + u"教师信息"

