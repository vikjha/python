from django.shortcuts import render, HttpResponse, redirect
  # the index function is called when root is visited
def index(request):
    response = "placeholder to later display all the list of blogs"
    return HttpResponse(response)

def new(request):
    response = "placeholder to display a new form to create a new blog"
    return HttpResponse(response)

def create(request):
    return redirect ('/blogs')

def show(request,id):
    response = "placeholder to display blog {}"
    return HttpResponse(response)

def edit(request,id):
    response = "placeholder to edit blog {}"
    return HttpResponse(response)

def destroy(request, id):
    return redirect ('/blogs')
