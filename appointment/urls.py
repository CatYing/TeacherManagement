from django.conf.urls import url
from appointment import views

urlpatterns = [
    url(r'^list/', views.TeacherListView.as_view(), name='list'),
]