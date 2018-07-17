from django.conf.urls import url
from .views import post_model_list_view

urlpatterns = [
    url(r'^$', post_model_list_view, name="list")
]
