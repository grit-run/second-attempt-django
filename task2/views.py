from django.shortcuts import render
from django.views.generic import TemplateView

# Functional View
def index_func(request):
    return render(request, 'func_template.html')

# Class Based View
class index_class(TemplateView):
    template_name = 'class_template.html'
