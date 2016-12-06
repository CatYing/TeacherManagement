from django.conf.urls import url
from authentication import views

urlpatterns = [
    url(r'^login/', views.login, name="login"),
    url(r'^logout/', views.logout, name="logout"),
    url(r'^student/update/', views.StudentInfoUpdateView.as_view(), name="stu_update"),
    url(r'^teacher/update/', views.TeacherInfoUpdateView.as_view(), name="tea_update"),
    url(r'^detail/', views.InfoDetailView.as_view(), name="detail"),
]