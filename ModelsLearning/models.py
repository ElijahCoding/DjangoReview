from django.db import models
from django.db.models import Model
from django.utils.encoding import smart_text
from django.utils import timezone
from .validators import validate_author_email
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save
from django.utils.timesince import timesince
from datetime import timedelta, datetime, date

PUBLISH_CHOICES = (
    ('draft', 'Draft'),
    ('publish', 'Publish'),
    ('private', 'Private')
)

# Create your models here.
class PostModel(Model):
    id = models.AutoField(primary_key=True)
    active = models.BooleanField(default=True)
    title = models.CharField(
        max_length=240,
        verbose_name='Post title',
        unique=True,
        error_messages={
            'unique': 'This title is not unique',
            'blank': 'This field is not full'
        },
        help_text='Must be a unique title'
    )
    slug = models.SlugField(null=True, blank=True, editable=False)
    content = models.TextField(null=True, blank=True)
    publish = models.CharField(max_length=120, choices=PUBLISH_CHOICES, default='draft')
    view_count = models.IntegerField(default=0)
    publish_date = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now)
    author_email = models.EmailField(max_length=240, validators=[validate_author_email], null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # if not self.slug and self.title:
        #     self.slug = slugify(self.title)
        super(PostModel, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __unicode(self):
        return smart_text(self.title)

    def __str__(self):
        return smart_text(self.title)

    def age(self):
        if self.publish == 'publish':
            now = datetime.now()
            publish_time = datetime.combine(
                self.publish_date,
                datetime.now().min.time()
            )
            try:
                difference = now - publish_time
            except:
                return 'Unknown'
            if difference <= timedelta(minutes=1):
                return 'just now'
            return '{time} ago'.format(time=timesince(publish_time)).split(', ')[0]
        return 'Not published'

def post_model_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug and instance.title:
        instance.slug = slugify(instance.title)

pre_save.connect(post_model_pre_save_receiver, sender=PostModel)

def post_model_post_save_receiver(sender, instance, created, *args, **kwargs):
    if created:
        if not instance.slug and instance.title:
            instance.slug = slugify(instance.title)
            instance.save()

post_save.connect(post_model_post_save_receiver, sender=PostModel)
