from django.db import models
import fts
from tinymce import models as tinymce_models

class Advantage(fts.SearchableModel):
    body = tinymce_models.HTMLField()
    published = models.BooleanField(u"Published", default=False)

    objects = fts.SearchManager()

    def __unicode__(self):
        return u"Adv: %s"%self.body[:100]
    str = __unicode__

    class Meta:
        pass

class Portal(models.Model):
    slogan = models.CharField(u"Slogan", max_length=1023, blank=False, null=False)
    phone =  models.CharField(u"Phone", max_length=255, blank=False, null=False)
    footer = tinymce_models.HTMLField()

    def __unicode__(self):
        return u"Portal meta-object"
