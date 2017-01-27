from django.shortcuts import render

# Create your views here.
def index(request): 
	return render(request, 'Lfit/index.html')

def clients(request): 
	return render(request, 'Lfit/clients.html')

def calendar(request): 
	return render(request, 'Lfit/calendar.html')

def training(request): 
	return render(request, 'Lfit/training.html')

def research(request): 
	return render(request, 'Lfit/research.html')








