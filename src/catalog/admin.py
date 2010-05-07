from django.contrib import admin
from catalog.models import *

class EquipmentAdmin(admin.ModelAdmin):
	list_display = ('code', 'name', 'cipher')
	search_fields = ['code', 'name', 'cipher']
admin.site.register(Equipment, EquipmentAdmin)
