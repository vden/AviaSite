from django.db import models
from fts.backends.simple import SearchableModel
from tinymce import models as tinymce_models

# Create your models here.

class Advantage(SearchableModel):
    body = tinymce_models.HTMLField()
    published = models.BooleanField(u"Published", default=False)

    def __unicode__(self):
        return u"Adv: %s"%self.body[:100]

    class Meta:
        pass
