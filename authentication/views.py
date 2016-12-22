from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import auth
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import HttpResponseRedirect
from django.views.generic import DetailView, UpdateView

from authentication.models import *
from notification.models import StudentNotificationsOnTeacher, StudentNotificationOnAppointment
from website.mixin import FrontMixin
from appointment.models import TeacherEnroll


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


def register(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse_lazy('index'))
    else:
        if request.method == "POST":
            if request.POST.get('tag') == '1':
                username = request.POST.get('username', '')
                password = request.POST.get('password', '')
                name = request.POST.get('name', '')
                teacher_id = request.POST.get('teacher_id', '')
                e_mail = request.POST.get('e_mail', '')
                cellphone = request.POST.get('cellphone', '')
                address = request.POST.get('address', '')
                if username and password and name and teacher_id and e_mail and cellphone and address:
                    new_user = User.objects.create_user(username=username, password=password)
                    new_user.save()
                    new_myuser = MyUser(
                        user=new_user,
                        name=name,
                        identity=2
                    )
                    new_myuser.save()
                    new_teacherinfo = TeacherInfo(
                        teacher_id=teacher_id,
                        e_mail=e_mail,
                        cellphone=cellphone,
                        address=address,
                        myuser=new_myuser,
                    )
                    new_teacherinfo.save()
                    new_stuonteacher = StudentNotificationsOnTeacher(
                        myuser=new_myuser
                    )
                    new_stuonteacher.save()
                    new_stuonapp = StudentNotificationOnAppointment(
                        myuser=new_myuser
                    )
                    new_teacher_enroll = TeacherEnroll(
                        teacher=new_myuser
                    )
                    new_teacher_enroll.save()
                    new_stuonapp.save()
            elif request.POST.get('tag') == '0':
                username = request.POST.get('username', '')
                password = request.POST.get('password', '')
                name = request.POST.get('name', '')
                student_id = request.POST.get('student_id', '')
                e_mail = request.POST.get('e_mail', '')
                cellphone = request.POST.get('cellphone', '')
                college = request.POST.get('college', '')
                grade = request.POST.get('grade', '')
                if username and password and name and student_id and e_mail and cellphone and college and grade:
                    new_user = User.objects.create_user(username=username, password=password)
                    new_user.save()
                    new_myuser = MyUser(
                        user=new_user,
                        name=name,
                        identity=1
                    )
                    new_myuser.save()
                    new_studentinfo = StudentInfo(
                        student_id=student_id,
                        e_mail=e_mail,
                        cellphone=cellphone,
                        college=college,
                        grade=grade,
                        myuser=new_myuser,
                    )
                    new_studentinfo.save()
                    new_stuonteacher = StudentNotificationsOnTeacher(
                        myuser=new_myuser
                    )
                    new_stuonteacher.save()
                    new_stuonapp = StudentNotificationOnAppointment(
                        myuser=new_myuser
                    )
                    new_stuonapp.save()
            return HttpResponseRedirect(reverse_lazy('login'))
        return render(request, 'authentication/register.html')


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

    def form_valid(self, form):
        for student in MyUser.objects.filter(identity=1):
            student.studentnotificationsonteacher.unread_count += 1
            student.studentnotificationsonteacher.save()
        return super(TeacherInfoUpdateView, self).form_valid(form)


