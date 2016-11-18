# coding=utf8

from django.conf.urls import url
from website import views

urlpatterns = [
    url('^$', views.IndexView.as_view(), name="index"),
]