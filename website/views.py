# coding=utf8

from django.views.generic import TemplateView
from website.mixin import FrontMixin
# Create your views here.


class IndexView(FrontMixin, TemplateView):
    template_name = 'website/index.html'
