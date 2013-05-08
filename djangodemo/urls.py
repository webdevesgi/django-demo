from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'crud.views.home'),
	url(r'^language/(?P<language>.+)/$', 'crud.views.language'),
	url(r'^framework/(?P<id>\d)/$', 'crud.views.framework'),
	url(r'^edit/(?P<id>\d)/$', 'crud.views.edit'),
    # url(r'^djangodemo/', include('djangodemo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)