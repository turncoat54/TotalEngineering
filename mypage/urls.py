#mypage/urls.py
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.iloveyjj, name='love'),
]