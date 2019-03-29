from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^search_by_name$', views.search_by_name, name='search_by_name'),
	url(r'^search_by_id$', views.search_by_id, name='search_by_id'),
    url(r'^modify$', views.modify, name='modify'),
    url(r'^log_in$', views.log_in, name='log_in'),
    url(r'^check_token$', views.check_token, name='check_token'),
    url(r'^dynamic_search$', views.dynamic_search, name='dynamic_search'),


]