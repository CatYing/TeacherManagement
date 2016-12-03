from django.shortcuts import render
from authentication.models import *
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.urlresolvers import reverse_lazy
# Create your views here.


class TeacherListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = MyUser
    context_object_name = 'teacher_list'
    login_url = reverse_lazy('login')
    template_name = 'appointment/list.html'

    def test_func(self):
        return self.request.user.myuser.identity == 1

    def get_queryset(self):
        return MyUser.objects.filter(identity=2)

    def get_context_data(self, **kwargs):
        context = super(TeacherListView, self).get_context_data(**kwargs)
        context['active'] = 'list'
        return context
