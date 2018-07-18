from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import PostModel

@login_required(login_url='/login/')
def post_model_list_view(request):
    qs = PostModel.objects.all()

    if request.user.is_authenticated():
        print('logged in')
    else:
        print('not logged in')

    if request.user.is_authenticated():
        template = 'blog/list-view.html'
    else:
        template = 'blog/list-view-public.html'

    context = { 'object_list': qs }
    return render(request, template, context)
