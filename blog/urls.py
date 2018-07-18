from django.conf.urls import url
from .views import (
    post_model_create_view,
    post_model_list_view,
    post_model_detail_view
)

app_name = 'blog'

urlpatterns = [
    url(r'^$', post_model_list_view, name="list"),
    url(r'^create/$', post_model_create_view, name="create"),
    url(r'^(?P<id>\d+)/$', post_model_detail_view, name="detail")
]
