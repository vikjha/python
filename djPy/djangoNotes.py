wsgi.py is used to show how django is served when deploying with heroku/aws ect

manage.py is the entry point to django commands within a project

django excells at creating Content management systems (CMS)

migrations are a way to move database from one configuration to another

db.sqlite is the database which automatically comes with django

HttpReponse is the class that represents an HTTP response back to the client.  it's the gateway to all of the other HTTP tools we have.

app is a self contained bit of functionality

a pluggable app is movable, can be plugged

change timezone in settings with list https://en.wikipedia.org/wiki/List_of_tz_database_time_zones

to make migrations on a specific app specificy the name like-- python manage.py migrate courses, for example

python manage.py shell opens a Python shell with Django's configuration already loaded.

Model.save() will save an in-memory instance of a model to the database.

Model.create() will save an in-memory instance of a model to the database and return the newly-created object.

Model.filter(attribute=value) will get a QuerySet of all instances of the Model that match the attribute values. You can change these values with other comparisons, too, like gte or in.

What does the auto_now_add attribute do?

sets date or time based field to current value when an instance is created_at

to create a user that can log into django Admin use: python manage.py createsuperuser

App-specific templates are best kept in a structure like app_name/templates/app_name because Django looks in app directories for a directory named templates and makes those templates automatically available.

{{ and }} are used to mark a variable you want printed out.

{% and %} mark template tags, or special bits of Python that Django's template engine knows how to run. Unlike Jinja2 templates, you can't just run arbitrary Python in a template.

render() turns a request object, a template, and an optional context dictionary into a generated string. More about render.

{% extends <template> %} - Template tag to specify which template the current one should inherit from.

{% block <name> %} and {% endblock %} - Template tag pair to mark a section of a parent template as overridable.

STATICFILES_DIRS is a setting for where to find static files. These files will either be served during development or will end up being collected by the collectstatic command during deployment.

staticfiles_urlpatterns() is a function that returns the URL patterns for static files based on DEBUG and a few other settings. You import it from django.contrib.staticfiles.urls.

{% load static from staticfiles %} - The way to import the {% static %} tag for use.

{% static "<path/to/asset>" %} - How to use the {% static %} tag to properly point to a static asset.

IntegerField is a field that holds integers, or whole numbers.

An inline is a smaller form inside of a larger form. The smaller form represents a related record in the database.

StackedInline is an inline where each field takes up the full width of the form. Fields are stacked.

TabularInline is an inline where each field is part of a single row for the form.

More docs on inlines.


{% for step in course.step_set.all %} Notice that we don't use the () on all(). You don't call functions in Django's template tags, the template engine will handle that for you.

Also, step_set is automatically generated from the foreign key. Handy!

Model.get(attribute=value) lets you get a single Model instance by a given attribute's value.

Here is more info on prefetch_related and select_related. Don't bother too much with these until you're comfortable with Django's ORM.

class Meta:
    ordering = ['field1', 'field2']
This will cause the model to be ordered by field1, then field2 if there are any conflicts on field1 (two instances having the same field1 value). Finally, they'll be sorted by id if a conflict still exists.

get_object_or_404(Model, [selectors]) - Gets an object of Model by using whatever selection arguments have been given. For example: get_object_or_404(User, username='kennethlove') would try to get a User with an username set to "kennethlove". If that User didn't exist, a 404 error would be raised.

What's the long way? Consider this view:

from django.http import Http404

from .models import Course

def course_detail(request, pk):
    try:
        course = Course.objects.get(pk=pk)
    except Course.DoesNotExist:
        raise Http404()
    else:
        return render(request, 'courses/course_detail.html', {'course': course})
It's definitely more work!
linebreaks is a filter that turns two returns in a row into HTML paragraph tags.

You apply filters to a variable with the pipe (|) character.

Our view needs an URL. Add a new url to article/urls.py. The pattern should be "article/" and then the pk argument, which should be one or more digits.

 url(r'article/(?P<pk>\d+)/$', views.article_detail),

 blank=True - A field can be blank (not filled in) in the admin and any other forms based on the model.

default='something' - If no value is supplied for the field, the default 'something' will be put into the record.

{% url 'path.to.view' %} to link to a view who's URL doesn't have a name.

Note: This has been removed in Django 1.10 and beyond. If you want to use this feature, be sure to install Django 1.9 or below. You can do that with pip install django<1.10. Better yet, name all of your URLs as shown below.

url(r'pattern', views.view, name='list') to name an URL

{% url 'list' %} to link to a named URL

include('courses.urls', namespace='course') to namespace a group of URLs

{% url 'courses:list' %} to link to a named and namespaced URL
