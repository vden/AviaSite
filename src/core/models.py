from django.db import models

# Create your models here.

class Advantage(models.Model):
    text = models.TextField(u"Text advantage", blank=False, null=False)
    published = models.BooleanField(u"Published", default=False)

    def __unicode__(self):
        return u"Adv: %s"%self.text[:100]

    class Meta:
        pass
