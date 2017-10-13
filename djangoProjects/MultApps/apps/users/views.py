# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse, redirect
# Create your views here.

def register(request):
    response = "placeholder for users to create a new user record"
    return HttpResponse(response)

def login(request):
    response = "placeholder for users to login"
    return HttpResponse(response)

def users(request):
    response = "placeholder for list of all users"
    return HttpResponse(response)
