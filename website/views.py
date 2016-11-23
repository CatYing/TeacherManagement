# coding=utf8
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from website.mixin import FrontMixin
# Create your views here.


class IndexView(LoginRequiredMixin, FrontMixin, TemplateView):
    template_name = 'website/index.html'
    login_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['active'] = 'index'
        return context
