from django.conf.urls import include, url
from blog import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	
	#register new user
	url(r'register/$', views.register, name='register'),
	#user login/logout/
	url(r'login/$', views.login, name='blog_login'),
	url(r'logout/$', views.logout, name='blog_logout'),
	url(r'admin_page/$', views.admin_page, name='admin_page'),
	#session
	url(r'^lousy-login/$', views.lousy_login, name='lousy_login'),
	url(r'^lousy-secret/$', views.lousy_secret, name='lousy_secret'),
	url(r'^lousy-logout/$', views.lousy_logout, name='lousy_logout'),
	#session
	url(r'test-delete/$', views.test_delete, name='test_delete'),
	url(r'test-session/$', views.test_session, name='test_session'),
	#cookie
	url(r'stop_tracking', views.stop_tracking, name='stop_tracking'),
	url(r'^track_user/$', views.track_user, name='track_user'),
	url(r'^track_user1/$', views.track_user1, name='track_user1'),
	url(r'^cookie/$', views.test_cookie, name='cookie'),
	
	url(r'^category/(?P<category_slug>[\w-]+)/$', views.post_by_category, name='post_by_category'),
	url(r'^tag/(?P<tag_slug>[\w-]+)/$', views.post_by_tag, name='post_by_tag'),
	url(r'^(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
	url(r'^$', views.post_list, name='post_list'),
	url(r'^time/$', views.today_is, name='todays_time'),
	url(r'^blog/$', views.test_redirect, name='test_redirect'),
	url(r'^feedback/$', views.feedback, name='feedback'),
	url(r'^myfeedback/$', views.myfeedback, name='myfeedback'),
]