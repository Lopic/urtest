# File encoding: utf-8

from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from models import Bug, Company, Project, Tester
from forms import BugForm


def bugs_list(request):
    bugs = Bug.objects.all()
    return render_to_response('buglist.html', {'bugs': bugs},
                              context_instance=RequestContext(request))


def add_bug(request):
    if request.method == 'POST':
        form = BugForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/bugs/')
    else:
        form = BugForm()
    return render_to_response('addbug.html',{'form': form},
                              context_instance=RequestContext(request))


# компании
def company_registraion(request):
    return render_to_response('company_registraion.html')

@login_required
def company_detail(request, pk):
    try:
        company = Company.objects.get(pk=pk)
    except Company.DoesNotExist:
        raise Http404
    projects = company.projects.all()
    return render_to_response('company_detail.html', locals(),
                              context_instance=RequestContext(request))

       
# тестеры
def tester_registraion(request):
    return render_to_response('tester_registraion.html')

@login_required
def tester_detail(request, pk):
    try:
        tester = Tester.objects.get(pk=pk)
    except Tester.DoesNotExist:
        raise Http404
    projects = tester.projects.all()
    return render_to_response('tester_detail.html', locals(),
                              context_instance=RequestContext(request))


# проекты
def new_project(request):
    return render_to_response('new_project.html')

@login_required
def project_detail(request, pk):
    try:
        project = Project.objects.get(pk=pk)
    except Project.DoesNotExist:
        raise Http404
    testers = project.testers.all()
    bugs = project.bugs.all()
    return render_to_response('project_detail.html', locals(),
                              context_instance=RequestContext(request))


