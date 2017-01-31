from django.shortcuts import render, redirect 
from django.contrib.auth.decorators import login_required

from Lfit.models import PersonalInfo
from .forms import PersonalInfoForm

# Create your views here.

def login_redirect(request):
	return redirect('/account/login')

#@login_required 
def index(request): 
	return render(request, 'Lfit/index.html')

#@login_required 
def clients(request): 
	if request.method == 'POST': 
		form = PersonalInfoForm(request.POST)
		if form.is_valid():
			return redirect(clients)
	return render(request, 'Lfit/clients.html')

#@login_required 
def calendar(request): 
	return render(request, 'Lfit/calendar.html')

#@login_required 
def training(request): 
	return render(request, 'Lfit/training.html')

#@login_required 
def research(request): 
	return render(request, 'Lfit/research.html')

#===#===#===#===#===#===#
#DEVELOPMENT VIEWS
#===#===#===#===#===#===#

def export(request):
	queryall = PersonalInfo.objects.all()
	#		print ('Landed on : ', name.first)
	return render(request, 'Lfit/export.html', {'queryall': queryall}) 

def personalinput(request):
	if request.method == 'POST': 
		form = PersonalInfoForm(request.POST)
		if form.is_valid():
			obj = PersonalInfo()
			obj.first = form.cleaned_data['first']
			obj.last = form.cleaned_data['last']
			obj.dob = form.cleaned_data['dob']
			obj.age = form.cleaned_data['age']
			obj.gender = form.cleaned_data['gender']
			obj.email = form.cleaned_data['email']
			obj.mobile = form.cleaned_data['mobile']
			obj.weightclass = form.cleaned_data['weightclass']
			obj.agecategory = form.cleaned_data['agecategory']
			obj.affiliatedivision = form.cleaned_data['affiliatedivision']
			obj.save()
			return redirect(index)
	else: 
		form = PersonalInfoForm()
		return render(request, 'Lfit/personalinput.html', {'form': form})	









