from django.db import models
import fts
from tinymce import models as tinymce_models

class News(fts.SearchableModel):
    title = models.CharField(u"Title", max_length=1023, blank=False, null=False)
    description = models.TextField(u"Short description", blank=True, null=True)
    body = tinymce_models.HTMLField()

    date = models.DateTimeField(u"Publishing date", blank=False, null=False)
    published = models.BooleanField(u"Published")

    photo = models.ImageField(u"Photo", blank=True, null=True, upload_to="photos/%Y/%m/%d")

    objects = fts.SearchManager( fields=('title','description', 'body') )

    def __unicode__(self):
        return self.title
    str = __unicode__


