from django.db import models

# Create your models here.

class Equipment(models.Model):
	code = models.IntegerField(u"System code", blank=True, null=True, primary_key=True)
	name = models.CharField(u"KI name", max_length=1024)
	cipher = models.CharField(u"Cipher", max_length=1024)
	draw_number = models.CharField(u"Draw number", max_length=1024, blank=True, null=True)
	soft_version = models.CharField(u"Soft version", max_length=1024, blank=True, null=True)
