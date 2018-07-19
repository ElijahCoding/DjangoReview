from django.db import models
from django.db.models import Model

# Create your models here.
class PostModel(Model):
    id = models.AutoField(primary_key=True)
    active = models.BooleanField(default=True)
    title = models.CharField(max_length=240)
    content = models.TextField(null=True, blank=True)
