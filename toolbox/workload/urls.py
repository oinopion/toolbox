# encoding: utf-8
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('toolbox.workload.views',
    url(r'^$', 'workload', name='workload'),
    url(r'^workload/$', 'workload'),
    url(r'^workload/(\d{4}-\d{2}-\d{2})/$', 'workload', name='workload_date'),

    url(r'^monthworkload/$', 'monthworkload', name='monthworkload'),
    url(r'^monthworkload/(\d{4}-\d{2}-\d{2})/$', 'monthworkload', name='monthworkload_date'),

    url(r'^projectload/$', 'projectload', name='projectload'),
    url(r'^projectload/(\d{4}-\d{2}-\d{2})/$', 'projectload', name='projectload_date'),

    url(r'^projectmonthload/$', 'projectmonthload', name='projectmonthload'),
    url(r'^projectmonthload/(\d{4}-\d{2}-\d{2})/$', 'projectmonthload', name='projectmonthload_date'),

    url(r'^assignment/$', 'create_assignment', name='create_assignment'),
)
