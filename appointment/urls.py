from django.conf.urls import url
from appointment import views

urlpatterns = [
    url(r'^list/', views.TeacherListView.as_view(), name='list'),
    url(r'^detail/(?P<pk>[0-9]+)', views.MyUserDetailView.as_view(), name='myuser-detail'),
    url(r'^free-time/(?P<pk>[0-9]+)', views.AppointmentCreateView.as_view(), name='preview'),
    url(r'stu-app-list/', views.StudentAppointmentListView.as_view(), name='stu-list'),
    url(r'tea-app-list/', views.TeacherAppointmentListView.as_view(), name='tea-list'),
]
