# encoding: utf-8
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('toolbox.stories.views',
    url(r'^$', 'stories_list', name='stories_list'),
    url(r'^(?P<pk>\d+)/move/$', 'importance_update', name='importance_update'),
)
