from django.conf.urls.defaults import *

urlpatterns = patterns('core.views',
	url(r'^sitemap/$', 'sitemap', name="core-sitemap"),
               (r'^$', 'index'),
)
