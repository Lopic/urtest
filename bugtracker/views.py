# File encoding: utf-8

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from models import Bug
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

def company_details(request,project):
    return render_to_response('company_details.html', {'pk': 13})

       #тестеры
def tester_registraion(request):
    return render_to_response('tester_registraion.html')

def testers_list(request):
    return render_to_response('testers_list.html', {'pk': 12})

def tester_details(request,project):
    return render_to_response('tester_details.html', {'pk': 22})

      # Пректы
def new_project(request):
    return render_to_response('new_project.html')

def projects_list(request):
    return render_to_response('projects_list.html', {'pk': 12})

def project_details(request,project):
    return render_to_response('project_details.html')


