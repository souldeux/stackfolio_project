from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'stackfolio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', include('stackyelp.urls', namespace='stackyelp')),
)
