from django.contrib import admin
from core.models import *

class AdvantageAdmin(admin.ModelAdmin):
	list_display = ('body', 'published')
	search_fields = ['body',]
admin.site.register(Advantage, AdvantageAdmin)
