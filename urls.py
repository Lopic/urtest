# File encoding: utf-8
from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.views.generic.simple import direct_to_template

# Родные для сайта виды
# Импорт делается автоматически
urlpatterns = patterns('urtest.bugtracker.views',
	(r'^$', direct_to_template, {'template': 'base.html'}),
    (r'^bugs/$', 'bugs_list'),
    (r'^bugs/add$', 'add_bug'),

    # Example:
    # (r'^urtest/', include('urtest.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)

# Статические файлы: CSS и тд
urlpatterns += patterns('',
	(r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': 'media'}),
)