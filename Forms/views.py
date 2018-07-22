from django.shortcuts import render

# Create your views here.
def form_index(request):
    template = 'test_form.html'
    context = {}
    return render(request, template, context)
