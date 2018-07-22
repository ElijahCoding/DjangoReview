from django.contrib import admin
from .models import PostModel

class PostModelAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'content',
        'publish',
        'publish_date',
        'active',
        'updated',
        'timestamp',
        'new_content'
    ]

    readonly_fields = ['updated', 'timestamp', 'new_content']

    def new_content(self, obj, *args, **kwargs):
        return str(obj.title)

    class Meta:
        model = PostModel

# Register your models here.
admin.site.register(PostModel, PostModelAdmin)
