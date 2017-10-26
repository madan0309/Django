from django.conf.urls import include, url
from cadmin import views

urlpatterns = [
	url(r'^post/add/$', views.post_add, name='post_add'),
	url(r'^post/update/(?P<pk>[\d]+)/$', views.post_update, name='post_update'),
]