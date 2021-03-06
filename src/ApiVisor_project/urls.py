from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^$', TemplateView.as_view(template_name='home.html')),
	url(r'^$', "apis.views.home",name='home'),
	# url(r'^settings', "apis.views.settings",name='settings'),
	url(r'^settings$', "apis.views.settings",name='settings'),
	url(r'^overview', TemplateView.as_view(template_name='overview.html'),name='overview'),
	# Examples:
	# url(r'^$', 'ApiVisor_project.views.home', name='home'),
	# url(r'^ApiVisor_project/', include('ApiVisor_project.foo.urls')),

	# Uncomment the admin/doc line below to enable admin documentation:
	# url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

	# Uncomment the next line to enable the admin:
	url(r'^admin/', include(admin.site.urls)),
	# url(r'^apis/', "apis.views.api_home"),
	url(r'^accounts/', include('registration.backends.default.urls')),
)

# Uncomment the next line to serve media files in dev.
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
	# import debug_toolbar
	# urlpatterns += patterns('',
	#                         url(r'^__debug__/', include(debug_toolbar.urls)),
	#                         )
