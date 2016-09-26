"""Simpl urls."""
from django.conf.urls import url

from views import index, requests

urlpatterns = [
    url(r'^index/', index, name='index'),
    url(r'^requests/', requests, name='requests'),
]
