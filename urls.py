from django.conf.urls.defaults import *
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    (r'^admin/', include(admin.site.urls)),

    (r'^tinymce/', include('tinymce.urls')),
    (r'^search/',include('core.urls')),
    (r'^$', include('core.urls')),

    (r'^news/', include('news.urls')),

    (r'^media/(?P<path>.*)', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

    url(r'^', include('cms.urls')),
)
