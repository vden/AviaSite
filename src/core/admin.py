from django.contrib import admin
from core.models import *
from news.models import *
from diagnosis.models import *

class AdvantageAdmin(admin.ModelAdmin):
	list_display = ('body', 'published')
	search_fields = ['body',]
admin.site.register(Advantage, AdvantageAdmin)


class NewsAdmin(admin.ModelAdmin):
	list_display = ('date', 'title', 'published')
	search_fields = ['date', 'title',]
admin.site.register(News, NewsAdmin)

class PortalAdmin(admin.ModelAdmin):
	list_display = ('phone', 'slogan')
	search_fields = []
admin.site.register(Portal, PortalAdmin)

class SystemAdmin(admin.ModelAdmin):
	list_display = ('title', "published")
admin.site.register(System, SystemAdmin)

class SystemBlockAdmin(admin.ModelAdmin):
	list_display = ('title', 'system', "published")
admin.site.register(SystemBlock, SystemBlockAdmin)
	
