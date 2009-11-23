# File encoding: utf-8

from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render_to_response
from models import Bug, Company, Project, Tester
from forms import BugForm

def bugs_list(request):
    bugs = Bug.objects.all()
    return render_to_response('buglist.html', {'bugs': bugs})

def add_bug(request):
    if request.method == 'POST':
        form = BugForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/bugs/')
    else:
        form = BugForm()
    return render_to_response('addbug.html',{'form': form})


       
# авторизация
def login(request):
    return render_to_response('login.html')

def logout(request):
    return render_to_response('logout.html')
       
# компании
def company_registraion(request):
    return render_to_response('company_registraion.html')

def companies_list(request):
    return render_to_response('companies_list.html', {'pk': 12})

def company_detail(request, pk):
    try:
	company = Company.objects.get(pk=pk)
    except Company.DoesNotExist:
	raise Http404
    projects = company.projects.all()
    return render_to_response('company_detail.html', locals())
       
# тестеры
def tester_registraion(request):
    return render_to_response('tester_registraion.html')

def testers_list(request):
    return render_to_response('testers_list.html', {'pk': 12})

def tester_details(request,project):
    return render_to_response('tester_details.html', {'pk': 22})
      
# проекты
def new_project(request):
    return render_to_response('new_project.html')

def projects_list(request):
    return render_to_response('projects_list.html')

def project_detail(request, pk):
    try:
        project = Project.objects.get(pk=pk)
    except Project.DoesNotExist:
        raise Http404
    testers = project.testers.all()
    bugs = project.bugs.all()
    return render_to_response('project_detail.html', locals())


