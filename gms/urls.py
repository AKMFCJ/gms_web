#-*- encoding:utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gms.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', include('xadmin.urls')),
)