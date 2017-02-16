from django.shortcuts import render, redirect, reverse, render_to_response
from django.contrib.auth.decorators import login_required

from Lfit.models import PersonalInfo, CycleCreate


from calendar import HTMLCalendar

from django.views.generic import TemplateView
from django.views.generic.edit import FormView


from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User 

from Lfit.graphs import Graph

from Client.forms import ImageUploadForm


#@login_required
class CustomView(TemplateView):

	def get(self, request): 

		#TWO STEPS: Querying both models

		user_id = User.objects.filter(username=request.user)[0]
		user_profile = PersonalInfo.objects.filter(user=user_id)[0]

		if self.template_name == 'Client/dashboard.html':
				cycle_data = CycleCreate.objects.filter(client=user_profile)[0]
				Graph.plot_user(user_id, cycle_data.bpcttot, cycle_data.dpcttot, cycle_data.spctot)
				context = {'user':request.user, 'userprofile':user_profile, 'cycle_data':cycle_data}
				return render(request, self.template_name, context)

		if self.template_name == 'Client/training.html':
				context = {}
				return render(request, self.template_name, context) 

		if self.template_name == 'Client/account.html':
				context = {'user':request.user, 'userprofile':user_profile}
				return render(request, self.template_name, context)

		return render(request, self.template_name)

	def post(self,request): 

		if self.template_name == "Client/account.html":
			form = ImageUploadForm(request.POST,request.FILES)
			if form.is_valid():
				obj = PersonalInfo.objects.get(user=request.user)
				obj.profile_pic = form.cleaned_data['image']
				obj.save()

		return redirect("/user/account")


def pie_plot(request):
	return render(request, 'Lfit/pie/louie.html')


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

