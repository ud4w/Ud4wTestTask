"""Simpl urls."""
from django.conf.urls import url
from django.http import HttpResponseRedirect
from views import index

urlpatterns = [
    url(r'^$', lambda r: HttpResponseRedirect('index/')),
    url(r'^index/$', index, name='index'),
]
