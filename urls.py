# File encoding: utf-8

from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.views.generic.simple import direct_to_template

# Родные для сайта виды
# Импорт делается автоматически
urlpatterns = patterns('urtest.bugtracker.views',
    # Главная страница
    (r'^$', direct_to_template, {'template': 'base.html'}),
    # Авторизация
    (r'^login$', 'login'),
    # Выход
    (r'^logout$', 'logout'),

    # Старые примеры работы с багами
    #(r'^bugs/$', 'bugs_list'),
    #(r'^bugs/add$', 'add_bug'),

    # Страницы для тестеров:
    # Список всех тестеров
    (r'^testers/$', 'testers_list'),
    # Личная страница тестера
    (r'^testers/(\d+)$', 'tester_details'),
    # Регистрация нового тестера
    (r'^testers/register$', 'tester_registraion'),

    # Страницы компаний:
    # Список всех компаний
    (r'^companies/$', 'companies_list'),
    # Личная страница компании
    (r'^companies/(\d+)$', 'company_details'),
    # Регистрация новой компании
    (r'^companies/register$', 'company_registraion'),

    # Страницы проектов:
    # Список всех проектов
    (r'^projects/$', 'projects_list'),
    # Страница проекта
    (r'^projects/(\d+)$', 'project_details'),
    # Добавление проекта
    (r'^projects/new$', 'new_project'),

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