from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import PostModel
from .forms import PostModelForm
from django.contrib import messages

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


def post_model_create_view(request):
    # if request.method == 'POST':
    #     form = PostModelForm(request.POST)
    #     if form.is_valid():
    #         form.save(commit=False)

    form = PostModelForm(request.POST or None)
    context = {
        "form": form
    }

    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        messages.success(request, 'created a new blog post')
        context = {
            "form": PostModelForm(request.POST or None)
        }
        # print(form.cleaned_data)
        # return HttpResponseRedirect("/blog/{num}".format(num=obj.id))

    template = "blog/create-view.html"
    return render(request, template, context)

def post_model_update_view(request, id=None):
    obj = get_object_or_404(PostModel, id=id)
    form = PostModelForm(request.POST or None, instance=obj)
    context = {
        "form": form
    }
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        messages.success(request, 'Updated post')
        return HttpResponseRedirect("/blog/{num}".format(num=obj.id))
    template = 'blog/update-view.html'
    return render(request, template, context)
