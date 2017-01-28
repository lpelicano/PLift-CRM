from django.shortcuts import render, redirect 
from django.contrib.auth.decorators import login_required


# Create your views here.

def login_redirect(request):
	return redirect('/account/login')

@login_required 
def index(request): 
	return render(request, 'Lfit/index.html')

@login_required 
def clients(request): 
	return render(request, 'Lfit/clients.html')

@login_required 
def calendar(request): 
	return render(request, 'Lfit/calendar.html')

@login_required 
def training(request): 
	return render(request, 'Lfit/training.html')

@login_required 
def research(request): 
	return render(request, 'Lfit/research.html')









