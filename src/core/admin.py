from django.contrib import admin
from core.models import *

class AdvantageAdmin(admin.ModelAdmin):
	list_display = ('text', 'published')
	search_fields = ['text',]
admin.site.register(Advantage, AdvantageAdmin)
