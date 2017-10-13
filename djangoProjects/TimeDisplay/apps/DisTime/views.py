# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from datetime import datetime

# Create your views here.
def index(req):

    timeFromMobo= datetime.now()

    context = {


        "currTime": timeFromMobo
    }

    return render(req, 'DisTime/index.html', context)
