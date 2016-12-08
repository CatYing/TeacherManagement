from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import DetailView
from django.views.generic import ListView, TemplateView
from appointment.models import *
from website.mixin import FrontMixin


class TeacherListView(LoginRequiredMixin, UserPassesTestMixin, FrontMixin, ListView):
    model = MyUser
    context_object_name = 'teacher_list'
    login_url = reverse_lazy('login')
    template_name = 'appointment/list.html'
    redirect_field_name = 'denied'

    def test_func(self):
        return self.request.user.myuser.identity == 1

    def get_queryset(self):
        return MyUser.objects.filter(identity=2)

    def get_context_data(self, **kwargs):
        context = super(TeacherListView, self).get_context_data(**kwargs)
        context['active'] = 'list'
        return context


class MyUserDetailView(LoginRequiredMixin, FrontMixin, DetailView):
    model = MyUser
    context_object_name = 'theuser'
    template_name = 'appointment/detail.html'
    login_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super(MyUserDetailView, self).get_context_data(**kwargs)
        context['active'] = 'list'
        return context


class AppointmentPreviewView(LoginRequiredMixin, UserPassesTestMixin, FrontMixin, DetailView):
    template_name = 'appointment/preview.html'
    context_object_name = 'teacher'
    model = MyUser
    login_url = reverse_lazy('login')
    redirect_field_name = 'denied'

    def test_func(self):
        return self.request.user.myuser.identity == 1

    def get_context_data(self, **kwargs):
        context = super(AppointmentPreviewView, self).get_context_data(**kwargs)
        context['active'] = 'list'
        context['time_list'] = TeacherPeriod.objects.filter(pk=self.kwargs.get(self.pk_url_kwarg))
        return context

