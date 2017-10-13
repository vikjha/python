# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Course, Step

class StepInline(admin.StackedInline):
    model = Step


class CourseAdmin(admin.ModelAdmin):
    inlines = [StepInline,]

admin.site.register(Course, CourseAdmin)
#admin.site.register(Step)



#use admin to add things to ur db without using the shell
