from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import PostModel
from .forms import PostModelForm
from django.contrib import messages

# Create your views here.
def post_model_robust_view(request, id=None):
    obj = none
    context = {}
    success_message = 'A new post was created'

    if id is None:
        template = 'blog/create-view.html'

    if id is not None:
        obj = get_object_or_404(PostModel, id=id)
        success_message = 'a new post was created'
        context["object"] = obj
        template = 'blog/detail-view.html'
        if "edit" in request.get_full_path():
            template = 'blog/update-view.html'

    if "delete" in request.get_full_path():
        template = "blog/delete-view.html"
        if request.method == 'POST':
            obj.delete()
            messages.success(request, 'Post deleted')
            return HttpResponseRedirect('/blog/')


    if "edit" in request.get_full_path() or "create" in request.get_full_path():
        form = PostModelForm(request.Post or None, instance=obj)
        context['form'] = form
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            messages.success(request, success_message)
            if obj is not None:
                return HttpResponseRedirect("/blog/{num}".format(obj.id))
            context['form'] = PostModelForm
    return render(request, template, context)


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


def post_model_delete_view(request, id=None):
    obj = get_object_or_404(PostModel, id=id)
    if request.method == 'POST':
        obj.delete()
        messages.success(request, 'post deleted')
        return HttpResponseRedirect("/blog/")
    context = {
        'object': obj
    }
    template = 'blog/delete-view.html'
    return render(request, template, context)
