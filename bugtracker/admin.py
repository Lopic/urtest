from django.contrib import admin
from urtest.bugtracker.models import Bug, Tester, Company, Project

admin.site.register(Bug)
admin.site.register(Tester)
admin.site.register(Company)
admin.site.register(Project)
