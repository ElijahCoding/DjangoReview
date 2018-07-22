from django.shortcuts import render
from .forms import SearchForm

# Create your views here.
def home(request):
    template = 'forms.html'
    context = { 'form': SearchForm() }
    return render(request, template, context)
