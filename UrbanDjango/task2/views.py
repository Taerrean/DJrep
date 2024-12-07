from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


def class_t(request):
    return render(request, 'class_template.html')


class FuncTemplate(TemplateView):
    template_name = 'func_template.html'
