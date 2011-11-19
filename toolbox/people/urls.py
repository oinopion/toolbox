# encoding: utf-8
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('toolbox.people.views',
    url(r'^$', 'people_list_view', name='people_list'),
    url(r'^(?P<pk>\d+)/$', 'person_detail_view', name='person_detail'),
)
