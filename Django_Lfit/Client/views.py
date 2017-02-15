from django.shortcuts import render, redirect, reverse, render_to_response
from django.contrib.auth.decorators import login_required

from Lfit.models import PersonalInfo, CompResults, Payments, CycleCreate, UserProfile
from Lfit.forms import PersonalInfoForm, CompResultsForm, PaymentsForm, CycleCreateForm  
from calendar import HTMLCalendar

from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from Lfit.graphs import Graph
import numpy as np
from mpld3 import fig_to_html
#from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas 

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User 


#@login_required
class CustomView(TemplateView):

	def get(self, request): 

		#TWO STEPS: Querying both models
		user_id = User.objects.filter(username=request.user)[0]
		user_profile = UserProfile.objects.filter(user=user_id)[0]

		if self.template_name == 'Client/dashboard.html':
				context = {'user':request.user, 'userprofile':user_profile}
				return render(request, self.template_name, context)

		if self.template_name == 'Client/training.html':
				query_live = CycleCreate.objects.filter(live='y')
				query_pending = CycleCreate.objects.filter(live='n')
				context = {'query_live':query_live, '`query_pending':query_pending}
				return render(request, self.template_name, context) 

		return render(request, self.template_name)


#===##===##===##===##===##===##===#
# Login VIEW
#===##===##===##===##===##===##===#
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .forms import CustomLoginForm
from django.template import RequestContext

def login_client(request):

	state = "Please login"

	if request.method == "POST" :
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			#===LOGIN CREDENTIALS were successful===#
			login(request, user)
			return redirect("/user/dashboard")

			#=====≠#  CUSTOM URL FOR UNIQUE USER #======#
			# return redirect("/%s/dashboard" % user)

		else:
			#===LOGIN CREDENTIALS have failed===#
			state = "Your name or password is not correct. Please try again"

	form = CustomLoginForm()
	return render(request,"Client/login.html", {"form":form,"state":state})

def logout_client(request):
	logout(request)
	return render(request, "Client/logout.html")

