from django.conf.urls.defaults import *

urlpatterns = patterns('news.views',
               (r'^$', 'index', {'page': None}),
               (r'^(?P<news_id>\d+)/', 'show_news'),
)
