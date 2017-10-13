from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login, name='do_the_login'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^register$', views.register),
    url(r'^success$', views.success),
    url(r'^user/(?P<user_id>\d+)$', views.show)
]
