from django import forms	

class PersonalInfoForm(forms.Form): 
	first =  forms.CharField(max_length=50)
	last = forms.CharField(max_length=50)
	dob = forms.DateField()
	age = forms.IntegerField()
	gender = forms.CharField(max_length=50)
	email = forms.CharField(max_length=50)
	mobile = forms.CharField(max_length=50)
	weightclass = forms.CharField(max_length=50)
	agecategory = forms.CharField(max_length=50)
	affiliatedivision = forms.CharField(max_length=50)	