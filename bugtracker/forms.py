from django import forms
import bugtracker.models as models

class BugForm(forms.ModelForm):
	class Meta:
		model = models.Bug
