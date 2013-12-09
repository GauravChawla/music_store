from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'music_store.views.home', name='home'),
    # url(r'^music_store/', include('music_store.foo.urls')),
    url(r'^login/', 'app.views.login'),
    url(r'^auth_it/', 'app.views.auth_view'),
    url(r'^register/', 'app.views.register'),
    url(r'^index/$', 'app.views.index'),
    url(r'^index/', 'app.views.index'),
    url(r'^logout/', 'app.views.logout'),
    url(r'^add_playlist/', 'app.views.add_playlist'),
    url(r'^playlist/', 'app.views.playlist'),
    url(r'^buy/', 'app.views.buy'),
    url(r'^route/', 'app.views.route'),
    url(r'^dashboard/', 'app.views.dashboard'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
