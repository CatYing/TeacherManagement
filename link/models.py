from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Link(models.Model):
    name = models.CharField(max_length=64)
    url = models.URLField()

    def __unicode__(self):
        return self.url
