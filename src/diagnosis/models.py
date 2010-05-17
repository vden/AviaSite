from django.db import models
import fts

class System(fts.SearchableModel):
    title = models.CharField(u"System name", max_length = 1023, blank = False, null = False)
    published = models.BooleanField(u"Published")

    def __unicode__(self):
        return self.title
    str = __unicode__

    def get_absolute_url(self):
        return "/repair/devices/%s/"%self.id

class SystemBlock(fts.SearchableModel):
    title = models.CharField(u"System block name", max_length = 2000, blank = False, null = False)
    system = models.ForeignKey(System)
    published = models.BooleanField(u"Published")

    def __unicode__(self):
        return self.title
    str = __unicode__

    def get_absolute_url(self):
        return "/repair/devices/%s/"%self.system.id

