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

