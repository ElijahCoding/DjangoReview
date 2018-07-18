from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import PostModel

# Create your views here.

# @login_required(login_url='/login/')
def post_model_list_view(request):
    qs = PostModel.objects.all()

    template = 'blog/list-view.html'
    context = { 'object_list': qs }

    return render(request, template, context)


def post_model_detail_view(request, id):
    # try:
    #     obj = PostModel.objects.get(id)
    # except:
    #     raise Http404

    obj = get_object_or_404(PostModel, id=id)
    context = { "object": obj }
    template = "blog/detail-view.html"
    return render(request, template, context)
