from django.conf.urls import patterns, include, url

from django.contrib import admin

from list.views import home_page
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', home_page, name='home'),
    url(r'^lists/(?P<list_id>\d+)/$', 'list.views.view_list',
        name='view_list'
    ),
    url(r'^lists/(?P<list_id>\d+)/add_item$', 'list.views.add_item',
        name='view_list'
    ),
    url(r'^lists/new$', 'list.views.new_list', name='new_list'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
