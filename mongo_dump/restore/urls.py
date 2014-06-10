from django.conf.urls.defaults import patterns, include, url
from .views import mongo_restore

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'restore.views.home', name='home'),
    # url(r'^restore/', include('restore.foo.urls')),
     url(r'^mongo_restore/', mongo_restore),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
