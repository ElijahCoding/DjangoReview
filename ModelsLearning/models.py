from django.db import models
from django.db.models import Model
from django.utils.encoding import smart_text
from django.utils import timezone

PUBLISH_CHOICES = (
    ('draft', 'Draft'),
    ('publish', 'Publish'),
    ('private', 'Private')
)

# Create your models here.
class PostModel(Model):
    id = models.AutoField(primary_key=True)
    active = models.BooleanField(default=True)
    title = models.CharField(max_length=240, unique=True)
    content = models.TextField(null=True, blank=True)
    publish = models.CharField(max_length=120, choices=PUBLISH_CHOICES, default='draft')
    view_count = models.IntegerField(default=0)
    publish_data = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __unicode(self):
        return smart_text(self.title)

    def __str__(self):
        return smart_text(self.title)
