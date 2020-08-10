from django.shortcuts import render
from validationapp import forms
from django.http import HttpResponseRedirect
# Create your views here.

def EmpViews(request):
	form=forms.EmpForms()
	if request.method=="POST":
		form=forms.EmpForms(request.POST)
		if form.is_valid():
			print("validation successfull...!")
			print(form.cleaned_data['Name'])
			print(form.cleaned_data['Sal'])
			print(form.cleaned_data['Loc'])
			print(form.cleaned_data['Add'])
			return HttpResponseRedirect('/thanks')
	else:
		form=forms.EmpForms()
	return render(request,'form.html',{'form':form})

def thanksviews(request):
	return render(request,'form1.html')