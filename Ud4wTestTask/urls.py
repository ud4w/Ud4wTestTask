"""Project level urls."""
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^index/', include('udaw_test.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
