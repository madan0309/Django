from django.conf.urls import include, url
from django.contrib import admin
from blog import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Examples:
    # url(r'^$', 'django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	
	url(r'', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^cadmin/', include('cadmin.urls')),
	
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
