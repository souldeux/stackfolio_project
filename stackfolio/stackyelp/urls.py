from django.conf.urls import patterns, include, url
from django.contrib import admin
from stackyelp import views

urlpatterns = patterns('',
	 url(r'^$', views.home, name='home'),
)
