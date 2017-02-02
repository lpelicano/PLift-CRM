from django.shortcuts import render, redirect 
from django.contrib.auth.decorators import login_required

from Lfit.models import PersonalInfo, CompResults, Payments, CycleCreate
from .forms import PersonalInfoForm, CompResultsForm, PaymentsForm, CycleCreateForm  
from calendar import HTMLCalendar


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
#===#===#===#===#===#===#
#
# DEVELOPMENT VIEWS
#
#===#===#===#===#===#===#
#===#===#===#===#===#===#


def export(request):
	queryall = PersonalInfo.objects.all()
	#		print ('Landed on : ', name.first)
	return render(request, 'Lfit/export.html', {'queryall': queryall}) 



# === Personal Details Form === #

def personalinput(request):
	if request.method == 'POST': 
		form = PersonalInfoForm(request.POST)
		print('FORM IS: ', form)
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
			return render(request, 'Lfit/personalinput.html', {'form': form})
	else: 
		form = PersonalInfoForm()
		return render(request, 'Lfit/personalinput.html', {'form': form})	

# === Competition Results Form === #
def compresultsinput(request):
	if request.method == 'POST': 
		form = CompResultsForm(request.POST)
		print('FORM IS: ', form)
		if form.is_valid():
			for key, value in form.cleaned_data.iteritems():
				print (key, value)
			return redirect(index)
		else:
			return render(request, 'Lfit/compresultsinput.html', {'form': form})
	else: 
		form = CompResultsForm()
		return render(request, 'Lfit/compresultsinput.html', {'form': form})	

# === Payments Form === #
def paymentsinput(request):
	if request.method == 'POST': 
		form = PaymentsForm(request.POST)
		print('FORM IS: ', form)
		if form.is_valid():
			for key, value in form.cleaned_data.iteritems():
				print(key, value)
			return redirect(index)
		else:
			return render(request, 'Lfit/paymentsinput.html', {'form': form})
	else: 
		form = PaymentsForm()
		return render(request, 'Lfit/paymentsinput.html', {'form': form})	


# === Cycle Creation Form === #
def cyclecreateinput(request):
	if request.method == 'POST': 
		form = CycleCreateForm(request.POST)
		print('FORM IS: ', form)
		if form.is_valid():
			for key, value in form.cleaned_data.iteritems():
				print(key, value)
			return redirect(index)
		else:
			return render(request, 'Lfit/cyclecreateinput.html', {'form': form})
	else: 
		form = CycleCreateForm()
		return render(request, 'Lfit/cyclecreateinput.html', {'form': form})	


def calendarpage(request): 
	cal = HTMLCalendar()
	monthly = cal.formatmonth(2016,5)
	return render(request, 'Lfit/calendarproto.html', {'monthly': monthly})

