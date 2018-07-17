from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import PostModel

def post_model_list_view(request):
    qs = PostModel.objects.all()
    return HttpResponse('fdas')
