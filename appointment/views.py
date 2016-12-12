from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.urlresolvers import reverse_lazy
from django.http import JsonResponse
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import ListView, TemplateView
from django.views.generic import UpdateView

from appointment.models import *
from notification.models import StudentNotificationOnAppointment, StudentNotificationsOnTeacher
from website.mixin import FrontMixin
import datetime


class TeacherListView(LoginRequiredMixin, UserPassesTestMixin, FrontMixin, ListView):
    model = MyUser
    context_object_name = 'teacher_list'
    login_url = reverse_lazy('login')
    template_name = 'appointment/list.html'
    redirect_field_name = 'denied'

    def test_func(self):
        return self.request.user.myuser.identity == 1

    def get_queryset(self):
        if self.request.GET.has_key('name'):
            return MyUser.objects.filter(identity=2, name__contains=self.request.GET.get('name'))
        return MyUser.objects.filter(identity=2)

    def get_context_data(self, **kwargs):
        context = super(TeacherListView, self).get_context_data(**kwargs)
        context['active'] = 'list'
        return context

    def get(self, request, *args, **kwargs):
        self.request.user.myuser.studentnotificationsonteacher.unread_count = 0
        self.request.user.myuser.studentnotificationsonteacher.save()
        return super(TeacherListView, self).get(request, *args, **kwargs)


class MyUserDetailView(LoginRequiredMixin, FrontMixin, DetailView):
    model = MyUser
    context_object_name = 'theuser'
    template_name = 'appointment/detail.html'
    login_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super(MyUserDetailView, self).get_context_data(**kwargs)
        context['active'] = 'list'
        return context


class AppointmentCreateView(LoginRequiredMixin, UserPassesTestMixin, FrontMixin, CreateView):
    template_name = 'appointment/preview.html'
    model = AppointmentObject
    login_url = reverse_lazy('login')
    redirect_field_name = 'denied'
    fields = []
    success_url = reverse_lazy('list')

    def test_func(self):
        return self.request.user.myuser.identity == 1 and AppointmentObject.objects.filter(student=self.request.user.myuser,
                                                                                           teacher_enroll=MyUser.objects.get(pk=self.kwargs.get(self.pk_url_kwarg)).teacherenroll,
                                                                                           result=1
                                                                                           ).count() == 0

    def get_context_data(self, **kwargs):
        context = super(AppointmentCreateView, self).get_context_data(**kwargs)
        context['active'] = 'list'
        context['time_list'] = TeacherPeriod.objects.filter(teacher=MyUser.objects.get(pk=self.kwargs.get(self.pk_url_kwarg)), free=True, date__gte=datetime.date.today())
        context['teacher'] = MyUser.objects.get(pk=self.kwargs.get(self.pk_url_kwarg))
        return context

    def form_valid(self, form):
        form.instance.student = self.request.user.myuser
        form.instance.teacher_enroll = MyUser.objects.get(pk=self.kwargs.get(self.pk_url_kwarg)).teacherenroll
        form.instance.teacher_period = TeacherPeriod.objects.get(pk=int(self.request.POST.get('teacher_period')))
        return super(AppointmentCreateView, self).form_valid(form)


class StudentAppointmentListView(LoginRequiredMixin, UserPassesTestMixin, FrontMixin, ListView):
    template_name = 'appointment/stu-app-list.html'
    model = AppointmentObject
    login_url = reverse_lazy('login')
    redirect_field_name = 'denied'
    context_object_name = 'app_list'

    def test_func(self):
        return self.request.user.myuser.identity == 1

    def get_queryset(self):
        return AppointmentObject.objects.filter(student=self.request.user.myuser)

    def get_context_data(self, **kwargs):
        context = super(StudentAppointmentListView, self).get_context_data(**kwargs)
        context['active'] = 'appointment'
        return context

    def get(self, request, *args, **kwargs):
        self.request.user.myuser.studentnotificationonappointment.unread_count = 0
        self.request.user.myuser.studentnotificationonappointment.save()
        return super(StudentAppointmentListView, self).get(request, *args, **kwargs)


class TeacherAppointmentListView(LoginRequiredMixin, UserPassesTestMixin, FrontMixin, ListView):
    template_name = 'appointment/tea-app-list.html'
    model = AppointmentObject
    login_url = reverse_lazy('login')
    redirect_field_name = 'denied'
    context_object_name = 'app_list'

    def test_func(self):
        return self.request.user.myuser.identity == 2

    def get_queryset(self):
        return AppointmentObject.objects.filter(teacher_enroll=self.request.user.myuser.teacherenroll)

    def get_context_data(self, **kwargs):
        context = super(TeacherAppointmentListView, self).get_context_data(**kwargs)
        context['active'] = 'appointment'
        return context

    def get(self, request, *args, **kwargs):
        if self.request.GET.has_key('pk'):
            appointment = AppointmentObject.objects.get(pk=int(self.request.GET.get('pk')))
            if self.request.GET.get('reply') == '1':
                appointment.result = 1
                appointment.student.studentnotificationonappointment.unread_count += 1
                appointment.student.studentnotificationonappointment.save()
                appointment.save()
            elif self.request.GET.get('reply') == '0':
                appointment.result = 0
                appointment.student.studentnotificationonappointment.unread_count += 1
                appointment.student.studentnotificationonappointment.save()
                for app in AppointmentObject.objects.filter(teacher_period=appointment.teacher_period):
                    app.result = 0
                    app.save()
                appointment.save()
        return super(TeacherAppointmentListView, self).get(request, *args, **kwargs)


class TeacherPeriodCreateView(LoginRequiredMixin, UserPassesTestMixin, FrontMixin, CreateView):
    login_url = reverse_lazy('login')
    redirect_field_name = 'denied'
    model = TeacherPeriod
    fields = ['date', 'free']
    template_name = 'appointment/time.html'
    success_url = reverse_lazy('tea-list')

    def test_func(self):
        return self.request.user.myuser.identity == 2

    def form_valid(self, form):
        form.instance.time_period = TimePeriod.objects.get(pk=int(self.request.POST.get('time_period')))
        form.instance.teacher = self.request.user.myuser
        return super(TeacherPeriodCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(TeacherPeriodCreateView, self).get_context_data(**kwargs)
        context['active'] = 'time'
        context['time'] = TimePeriod.objects.all()
        return context


class TeacherPeriodListView(LoginRequiredMixin, UserPassesTestMixin, FrontMixin, ListView):
    login_url = reverse_lazy('login')
    redirect_field_name = 'denied'
    model = TeacherPeriod
    template_name = 'appointment/admin-time.html'
    context_object_name = 'time_list'

    def test_func(self):
        return self.request.user.myuser.identity == 2

    def get_queryset(self):
        return TeacherPeriod.objects.filter(teacher=self.request.user.myuser, date__gte=datetime.date.today())

    def get_context_data(self, **kwargs):
        context = super(TeacherPeriodListView, self).get_context_data(**kwargs)
        context['active'] = 'admin-time'
        return context
