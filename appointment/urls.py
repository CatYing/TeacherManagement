from django.conf.urls import url
from appointment import views

urlpatterns = [
    url(r'^list/', views.TeacherListView.as_view(), name='list'),
    url(r'^detail/(?P<pk>[0-9]+)', views.MyUserDetailView.as_view(), name='myuser-detail'),

]