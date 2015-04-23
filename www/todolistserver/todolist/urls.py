#!/usr/bin/python
#coding=utf-8
#-*- coding: UTF-8 -*- 


from django.conf.urls import *
from django.contrib import admin
from todolistapp import views
from django.conf import settings

#urlpatterns = [
    # Examples:
    # url(r'^$', 'todolist.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    
    #url(r'^admin/', include('django.contrib.admin.urls')),
 #   url(r'^admin/', include(admin.site.urls)),
    
#]



urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
	url(r'^$', views.todolist, name='todo'),
    url(r'^addtodo/$', views.addTodo, name='add'),
    url(r'^finish/(?P<id>\d+)/$', views.todofinish, name='finish'),
    url(r'^backout/(?P<id>\d+)/$', views.todoredo,  name='backout'),
    url(r'^update/(?P<id>\d+)/$', views.updatetodo, name='update'),
    url(r'^delete/(?P<id>\d+)/$', views.tododelete, name='delete'),
    url(r'^redirfordelete/$',views.todolist,name='redirdelete'),
    url(r'^redirforfinish/$', views.todolist,name='redirfinish'),
    url(r'^redirforredo/$', views.todolist,name='redirredo'),
    url(r'^redirupdate/$', views.todolist,name='redirupdate'),
	)


if settings.DEBUG:
	import debug_toolbar
	urlpatterns += patterns('',
		url(r'^__debug__/',include(debug_toolbar.urls)),
		)

	DEBUG_TOOLBAR_PANELS = [
        'debug_toolbar.panels.versions.VersionsPanel',
        'debug_toolbar.panels.timer.TimerPanel',
        'debug_toolbar.panels.settings.SettingsPanel',
        'debug_toolbar.panels.headers.HeadersPanel',
        'debug_toolbar.panels.request.RequestPanel',
        'debug_toolbar.panels.sql.SQLPanel',
        'debug_toolbar.panels.staticfiles.StaticFilesPanel',
        'debug_toolbar.panels.templates.TemplatesPanel',
        'debug_toolbar.panels.cache.CachePanel',
        'debug_toolbar.panels.signals.SignalsPanel',
        'debug_toolbar.panels.logging.LoggingPanel',
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ]



