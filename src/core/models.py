from django.db import models
import fts
from tinymce import models as tinymce_models
from django.utils.translation import ugettext_lazy as _


class Advantage(fts.SearchableModel):
    body = tinymce_models.HTMLField()
    published = models.BooleanField(_("Published"), default=False)

    objects = fts.SearchManager()

    def __unicode__(self):
        return u"Adv: %s"%self.body[:100]
    str = __unicode__

    def get_absolute_url(self):
	return u"/"

    class Meta:
        pass

class Portal(models.Model):
    slogan = models.CharField(_("Slogan"), max_length=1023, blank=False, null=False)
    phone =  models.CharField(_("Phone"), max_length=255, blank=False, null=False)
    footer = tinymce_models.HTMLField()
    advertising_title =  models.CharField(_("Advertising title"), max_length=255, blank=False, null=False)
  #  advertising_body = tinymce_models.HTMLField()

    def __unicode__(self):
        return u"Portal meta-object"

#    def save(self):
     #   if len(Portal.objects.all()):
      #      raise Exception(_("Only one portal object can be created!"))

