from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'me_and_max.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^producers/', 'catalog.views.producers', name='producers'),
    url(r'^producer/(\d+)/', 'catalog.views.producer', name='producer'),

    url(r'^admin/', include(admin.site.urls)),
)
