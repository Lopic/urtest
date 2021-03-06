# File encoding: utf-8

from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.views.generic.simple import direct_to_template
from django.views.generic import list_detail
from urtest.bugtracker.models import Project, Company, Tester

project_info = {
	"queryset": Project.objects.all(),
	"template_name": "project_list.html",
	"template_object_name": "project",
}

company_info = {
	"queryset": Company.objects.all(),
	"template_name": "company_list.html",
	"template_object_name": "company",
}

tester_info = {
	"queryset": Tester.objects.all(),
	"template_name": "tester_list.html",
	"template_object_name": "tester",
}

# Родные для сайта виды
# Импорт делается автоматически
urlpatterns = patterns('urtest.bugtracker.views',
    # Главная страница
    (r'^$', direct_to_template, {'template': 'base.html'}),

    # Старые примеры работы с багами
    (r'^bugs/$', 'bugs_list'),
    (r'^bugs/add$', 'add_bug'),

    # Страницы для тестеров:
    # Список всех тестеров
    (r'^testers/$', list_detail.object_list, tester_info),
    # Личная страница тестера
    (r'^testers/(\d+)$', 'tester_detail'),
    # Регистрация нового тестера
    (r'^testers/register$', 'tester_registraion'),

    # Страницы компаний:
    # Список всех компаний
    (r'^companies/$', list_detail.object_list, company_info),
    # Личная страница компании
    (r'^companies/(\d+)$', 'company_detail'),
    # Регистрация новой компании
    (r'^companies/register$', 'company_registraion'),

    # Страницы проектов:
    # Список всех проектов
    (r'^projects/$', list_detail.object_list, project_info),
    # Страница проекта
    (r'^projects/(\d+)', 'project_detail'),
    # Добавление проекта
    (r'^projects/new$', 'new_project'),

    # Example:
    # (r'^urtest/', include('urtest.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
)

urlpatterns += patterns('',
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('django.contrib.auth.views',
    # Авторизация
    (r'^login$', 'login', {'template_name': 'login.html'}),
    # Выход
    (r'^logout$', 'logout', {'template_name': 'logout.html'}),
)

# Статические файлы: CSS и тд
urlpatterns += patterns('',
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
       {'document_root': 'media'}),

)
