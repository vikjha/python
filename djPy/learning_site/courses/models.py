# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Course(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length= 255)
    description = models.TextField()

    def __str__(self):#str method defines how this thing turns into a string, how to describe so in this case with the query set will return Course:Title when doing Course.objects.all()
        return self.title

class Step(models.Model):
    title = models.CharField(max_length= 255)
    description = models.TextField()
    content = models.TextField(blank = True, default = '')#blank equal true leaves the textfield optional, and default '' is the data shown an empty string if no data is entered
    order = models.IntegerField(default=0)
    course = models.ForeignKey(Course)


    class Meta:
        ordering = ['order', ]

    def __str__(self):
        return self.title
