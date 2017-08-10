from __future__ import unicode_literals
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateTimeField()

    def __unicode__(self):
        return self.title
    # This just returns the title

    # def __str__ is for Python 3
    # def __unicode__ is for python 2

# Create your models here.
