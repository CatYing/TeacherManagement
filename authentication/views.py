from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import auth
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import HttpResponseRedirect
from django.views.generic import DetailView, UpdateView

from authentication.models import *
from website.mixin import FrontMixin


def login(request):
    if request.GET.get('denied'):
        return render(request, 'website/denied.html', context={'myuser': request.user.myuser})
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse_lazy("index"))
    else:
        state = ""
        user = None
        if request.method == "POST":
            username = request.POST.get("username", "")
            password = request.POST.get("password", "")
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return HttpResponseRedirect(reverse_lazy("index"))
            else:
                state = "error"
        content = {
            'user': user,
            'state': state
        }
        return render(request, 'authentication/login.html', content)


@login_required(login_url=reverse_lazy('login'))
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse_lazy("login"))


class InfoDetailView(LoginRequiredMixin, FrontMixin, DetailView):
    context_object_name = 'user'
    template_name = 'authentication/detail.html'
    login_url = reverse_lazy("login")

    def get_object(self, queryset=None):
        return self.request.user.myuser

    def get_context_data(self, **kwargs):
        context = super(InfoDetailView, self).get_context_data(**kwargs)
        context['active'] = 'detail'
        return context


class StudentInfoUpdateView(UserPassesTestMixin, FrontMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = StudentInfo
    context_object_name = 'info'
    fields = ['student_id', 'e_mail', 'cellphone', 'college', 'grade', 'description']
    template_name = 'authentication/update.html'
    success_url = reverse_lazy('detail')
    redirect_field_name = 'denied'

    def test_func(self):
        return self.request.user.myuser.identity == 1

    def get_object(self, queryset=None):
        return self.request.user.myuser.studentinfo

    def get_context_data(self, **kwargs):
        context = super(StudentInfoUpdateView, self).get_context_data(**kwargs)
        context['active'] = 'detail'
        return context


class TeacherInfoUpdateView(UserPassesTestMixin, FrontMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = TeacherInfo
    context_object_name = 'info'
    fields = ['e_mail', 'cellphone', 'address', 'description']
    template_name = 'authentication/update.html'
    success_url = reverse_lazy('detail')
    redirect_field_name = 'denied'

    def test_func(self):
        return self.request.user.myuser.identity == 2

    def get_object(self, queryset=None):
        return self.request.user.myuser.teacherinfo

    def get_context_data(self, **kwargs):
        context = super(TeacherInfoUpdateView, self).get_context_data(**kwargs)
        context['active'] = 'detail'
        return context


