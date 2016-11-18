from django.conf.urls import url
from authentication import views

urlpatterns = [
    url(r'^login/', views.login, name="login"),
    url(r'^logout/', views.logout, name="logout"),
    url(r'^update/', views.StudentInfoUpdateView.as_view(), name="update"),
    url(r'^detail/', views.InfoDetailView.as_view(), name="detail"),
]