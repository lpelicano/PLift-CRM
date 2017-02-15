from django import forms
from Lfit.models import PersonalInfo, CompResults, Payments, CycleCreate 
# from django.forms import CharField, DateField, IntegerField, ChoiceField, DecimalField

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

#===#===#===#===#===#===#
# Clients
#===#===#===#===#===#===#

class PersonalInfoForm(forms.ModelForm):
	class Meta:
		model = PersonalInfo
		fields = ['user','first', 'last', 'dob', 'age', 'gender', 
		'email', 'mobile', 'weightclass', 'agecategory',
		'affiliatedivision']

#===#===#===#===#===#===#
# Competition Results
#===#===#===#===#===#===#

class CompResultsForm(forms.ModelForm):
	class Meta:
		model = CompResults
		fields = ['client', 'compdate', 'compname', 
		'complocation', 'bodyweight', 'weightclass', 'sq1', 
		'sq2', 'sq3', 'bp1', 'bp2', 'bp3', 'dl1', 'dl2', 'dl3', 
		'comptotal', 'wilks']

#===#===#===#===#===#===#
# Payments Results
#===#===#===#===#===#===#

class PaymentsForm(forms.ModelForm):
	class Meta:
		model = Payments
		fields = ['paymentdate','client', 'cyclename',
		'payplan', 'weeks', 'totaltopay', 'paid', 'paymentmethod']

#===#===#===#===#===#===#
# Cycle Creation
#===#===#===#===#===#===#

class CycleCreateForm(forms.ModelForm):
	class Meta:
		model = CycleCreate
		fields = ['client', 'startdate', 'enddate',
		'trainingtype', 'days', 'weeks', 'sslots', 'bslots',
		'dslots', 'spctot', 'bpcttot', 'dpcttot', 'smpct', 
		'svpct', 'sspct', 'bmpct', 'bv1pct', 'bv2pct', 'bs1pct',
		'bs2pct', 'dmpct', 'dvpct', 'dspct', 'smApct', 
		'svApct', 'ssApct', 'bmApct', 'bv1Apct', 'bv2Apct',
		'bs1Apct', 'bs2Apct', 'dmApct', 'dvApct', 'dsApct', 
		'smmov', 'svmov', 'ssmov', 'bmmov', 'bv1mov', 'bv2mov',
		'bs1mov', 'bs2mov', 'dmmov', 'dvmov', 'dsmov', 'smAmov', 
		'svAmov', 'ssAmov', 'bmAmov', 'bv1Amov', 'bv2Amov',
		'bs1Amov', 'bs2Amov', 'dmAmov', 'dvAmov', 'dsAmov',]

class CustomLoginForm(AuthenticationForm):
	class Meta: 
		model = User

	def __init__(self, *args, **kwargs):
		super(MyForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget.attrs.update({'class' : 'myfieldclass'})
		self.fields['password'].widget.attrs.update({'class' : 'myfieldclass'})


#====#====##====#====##====#====##====#====#
# REGISTRATION FORM DEVELOPMENT
#====#====##====#====##====#====##====#====#

from django import forms 
from django.contrib.auth.models import User

class UserProfileForm(forms.ModelForm):
	class Meta: 
		model = User 
		fields = ['first_name', 'last_name', 'email']











