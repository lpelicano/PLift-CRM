from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required

from Lfit.models import PersonalInfo, CompResults, Payments, CycleCreate
from .forms import PersonalInfoForm, CompResultsForm, PaymentsForm, CycleCreateForm  
from calendar import HTMLCalendar

from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from .graphs import Graph
import numpy as np
from mpld3 import fig_to_html
#from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas 

#@login_required
class CustomView(TemplateView):

	def get(self, request): 
		if self.template_name == 'Lfit/clients.html':
				query_personal = PersonalInfo.objects.all()
				query_comp = CompResults.objects.all()
				query_payments = Payments.objects.all()
				context = {'query_personal':query_personal, 'query_comp':query_comp, 'query_payments':query_payments, 'user':request.user}
				return render(request, self.template_name, context)

		if self.template_name == 'Lfit/training.html':
				query_live = CycleCreate.objects.filter(live='y')
				query_pending = CycleCreate.objects.filter(live='n')
				context = {'query_live':query_live, '`query_pending':query_pending}
				return render(request, self.template_name, context) 
		print('Template name: ', self.template_name)
		return render(request, self.template_name)

	def post(self, request):

		if self.template_name == 'Lfit/training.html':
			print("REQUEST: " , request.POST)
			print(request.POST['cycle'])
			cycle = CycleCreate.objects.get(cyclename = request.POST['cycle'])			
			print ('live: ' , cycle.live)
			if cycle.live == 'y':
				cycle.live = 'n'
			else:
				cycle.live = 'y'
			cycle.save()

			return redirect("/account/training")

def research(request): 
	# plt,fig,ax,figure = Main.plotgraph()
	#canvas = FigureCanvas(fig)
	return render(request, 'Lfit/research.html')#, {'figure':figure})
	 
# Create your views here.

def line_graph(request):
	return render(request, 'Lfit/S2B.html')


def login_redirect(request):
	return redirect('/account/login')

#===#===#===#===#===#===#===#===#===#===#===#===#===#===#===#===#===#===#
#===#===#===#===#===#===#===#===#===#===#===#===#===#===#===#===#===#===#
#
# DEVELOPMENT VIEWS
#
#===#===#===#===#===#===#===#===#===#===#===#===#===#===#===#===#===#===#
#===#===#===#===#===#===#===#===#===#===#===#===#===#===#===#===#===#===#


def export(request):
	queryall = PersonalInfo.objects.all()
	#		print ('Landed on : ', name.first)
	return render(request, 'Lfit/export.html', {'queryall': queryall}) 


# === Personal Details Form ============================== #

def personalinput(request):
	if request.method == 'POST': 
		form = PersonalInfoForm(request.POST)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.save()
			return redirect('/account/home')
		else:
			return render(request, 'Lfit/personalinput.html', {'form': form})
	else: 
		form = PersonalInfoForm()
		return render(request, 'Lfit/personalinput.html', {'form': form})	

# === Competition Results Form =========================== #
def compresultsinput(request):
	if request.method == 'POST': 
		form = CompResultsForm(request.POST)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.save
			return redirect('/account/home')
		else:
			return render(request, 'Lfit/compresultsinput.html', {'form': form})
	else: 
		form = CompResultsForm()
		return render(request, 'Lfit/compresultsinput.html', {'form': form})	

# === Payments Form ======================================= #
def paymentsinput(request):
	if request.method == 'POST': 
		form = PaymentsForm(request.POST)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.save()
			return redirect('/account/home')
		else:
			return render(request, 'Lfit/paymentsinput.html', {'form': form})
	else: 
		form = PaymentsForm()
		return render(request, 'Lfit/paymentsinput.html', {'form': form})	


# === Cycle Creation Form ================================= #
def cyclecreateinput(request):
	if request.method == 'POST': 
		form = CycleCreateForm(request.POST)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.save()
			return redirect('/account/home')
		else:
			return render(request, 'Lfit/cyclecreateinput.html', {'form': form})
	else: 
		form = CycleCreateForm()
		return render(request, 'Lfit/cyclecreateinput.html', {'form': form})	



# === Calendarrrrr???????? ================================= #

def calendarpage(request): 
	cal = HTMLCalendar()
	monthly = cal.formatmonth(2016,5)
	return render(request, 'Lfit/calendarproto.html', {'monthly': monthly})


#====Basic VIEWS (Original) ====# 

#@login_required 
# def index(request): 
# 	return render(request, 'Lfit/index.html')

# #@login_required 
# def clients(request): 
# 	if request.method == 'POST': 
# 		form = PersonalInfoForm(request.POST)
# 		if form.is_valid():
# 			return redirect(clients)
# 	return render(request, 'Lfit/clients.html')

# #@login_required 
# def calendar(request): 
# 	return render(request, 'Lfit/calendar.html')

# #@login_required 
# def training(request): 
# 	return render(request, 'Lfit/training.html')

# #@login_required 
# def research(request): 
# 	return render(request, 'Lfit/research.html')

# def forms_nav(request):
# 	return render(request, 'Lfit/forms_nav.html')

#====#=====#====# Advanced Custom Form View Function #====#=====#====#=====#


# class CustomFormView(FormView): 
# 	# template_name = 'Lfit/personalinput.html'
# 	form_class = PersonalInfoForm
# 	success_url = '/home'
# 	initial = {'key':'value'}

# 	def get(self, request, *args, **kwargs):
# 		form = self.form_class(initial=self.initial)
# 		print (self.get_form_class())
# 		return render(request, self.template_name, {'form': form})

# 	def form_valid(self, form): 
# 		obj = form.save(commit = False)
# 		obj.save()
# 		return redirect('/account/home')


#====#====##====#====##====#====##====#====#
# REGISTRATION FORM DEVELOPMENT
#====#====##====#====##====#====##====#====#

from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import UserProfile
from Lfit.forms import UserProfileForm
from django.forms.models import inlineformset_factory
from django.core.exceptions import PermissionDenied

@login_required
def edit_user(request, pk):
    user = User.objects.get(pk=pk)
    user_form = UserProfileForm(instance=user)
 
    ProfileInlineFormset = inlineformset_factory(User, UserProfile, fields=('phone', 'city', 'organization'))
    formset = ProfileInlineFormset(instance=user)

    if request.user.is_authenticated() and request.user.id == user.id:
        print ("authenicated")
        if request.method == "POST":
            user_form = UserProfileForm(request.POST, request.FILES, instance=user)
            formset = ProfileInlineFormset(request.POST, request.FILES, instance=user)
 
            if user_form.is_valid():
                created_user = user_form.save(commit=False)
                formset = ProfileInlineFormset(request.POST, request.FILES, instance=created_user)
 
                if formset.is_valid():
                    created_user.save()
                    formset.save()
                    return HttpResponseRedirect('/account/home')
 
        return render(request, "Lfit/update_info.html", {
            "noodle": pk,
            "noodle_form": user_form,
            "formset": formset,
        })
    else:
        raise PermissionDenied