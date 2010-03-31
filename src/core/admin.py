from django.contrib import admin
from core.models import *
from news.models import *

class AdvantageAdmin(admin.ModelAdmin):
	list_display = ('body', 'published')
	search_fields = ['body',]
admin.site.register(Advantage, AdvantageAdmin)


class NewsAdmin(admin.ModelAdmin):
	list_display = ('date', 'title', 'published')
	search_fields = ['date', 'title',]
admin.site.register(News, NewsAdmin)
