from django.conf.urls import patterns, include, url

from django.contrib import admin

from list.views import home_page
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', home_page, name='home'),
    url(r'^lists/', include('list.urls')),
    
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
