from django import forms
import bugtracker.models as models

class BugForm(forms.ModelForm):
	class Meta:
                exclude = ['tester']
		model = models.Bug


class ProjectForm(forms.ModelForm):
        class Meta:
                exclude = ['company']
		model = models.Project

class TesterForm(forms.ModelForm):
        class Meta:
                model = models.Tester

class CompanyForm(forms.ModelForm):
        class Meta:
                model = models.Company