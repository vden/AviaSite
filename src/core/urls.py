from django.conf.urls.defaults import *

urlpatterns = patterns('core.views',
               (r'^(?P<search_string>.*)/', 'search'),
               (r'^$', 'index'),
)
