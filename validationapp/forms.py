from django import forms

class EmpForms(forms.Form):
	Name=forms.CharField()
	Sal=forms.FloatField()
	Loc=forms.CharField()
	Add=forms.CharField()