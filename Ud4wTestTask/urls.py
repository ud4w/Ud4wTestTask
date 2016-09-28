"""Project level urls."""
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^', include('udaw_test.urls', namespace="udaw_test")),
    url(r'^admin/', include(admin.site.urls)),
)
