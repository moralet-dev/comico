from django.shortcuts import render
from django.views.generic import *


def index(request):
    return render(request, 'store/index.html', {})


class IndexView(ListView):
    template_name = 'store/index.html'

