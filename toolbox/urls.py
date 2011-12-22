from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

admin.autodiscover()

homepage = TemplateView.as_view(template_name="homepage.html")

urlpatterns = patterns('',
    url(r'^$', homepage, name='home'),
    url(r'^workload/', include('toolbox.workload.urls')),
    url(r'^people/', include('toolbox.people.urls')),
    url(r'^stories/', include('toolbox.stories.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    media_root = {'document_root': settings.MEDIA_ROOT}
    static_root = {'document_root': settings.STATIC_ROOT}
    urlpatterns += patterns('django.views.static',
        url(r'^media/(?P<path>.*)$', 'serve', media_root),
        url(r'^static/(?P<path>.*)$', 'serve', static_root),
    )
