from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^(?P<list_id>\d+)/$', 'list.views.view_list',
        name='view_list'
    ),
    url(r'^new$', 'list.views.new_list', name='new_list'),
)