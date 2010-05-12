from django.conf.urls.defaults import *

urlpatterns = patterns('core.views',
	(r'^sitemap/$', 'sitemap'),
               (r'^$', 'index'),
)
