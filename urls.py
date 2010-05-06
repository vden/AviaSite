from django.conf.urls.defaults import *
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    (r'^admin/', include(admin.site.urls)),

    (r'^tinymce/', include('tinymce.urls')),
    (r'^search/', 'core.views.search'),
    url(r'^repair/devices/(?P<device_id>\d+)/', 'diagnosis.views.device_info', name="device_info"),
    url(r'^repair/devices/', 'diagnosis.views.index', name="device_index"),
    url(r'^repair/order/', 'orders.views.repair', name="repair_order"),
    url(r'^ati/order/', 'orders.views.ati', name="ati_order"),

    (r'^news/', include('news.urls')),

    (r'^$', include('core.urls')),

    (r'^media/(?P<path>.*)', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

    url(r'^', include('cms.urls')),
)
