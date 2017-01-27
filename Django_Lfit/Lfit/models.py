from django.db import models
from django.db.models import CharField, DateField, IntegerField, TextField, EmailField, DecimalField

# Create your models here.

# CHOICES >
	# .. Clients
gender_choices = (('m', 'male'), ('f', 'female'),)
payplan_choices = (('12', '12'), ('14', '14'),)
paid_choices = (('y', 'yes'),('n', 'no'),)
method_choices = (('cash', 'cash'),('pp', 'paypal'),('bank', 'bank transfer'),)
	# .. Training
live_choices = (('y', 'yes'),('n', 'no'),)
trainingtype_choices = (('t','TRAINING'), ('o', 'OFFSEASON'), ('p', 'PEAKING'),)



#MAIN > Overview
#MAIN > Overview (Widget)
#MAIN > Small Calendar (Widget)
#MAIN > News

#CLIENTS > Personal Info
class PersonalInfo(models.Model):
	first =  CharField(max_length=50, null=True)
	last = CharField(max_length=50, null=True)
	dob = DateField(null=True)
	age = IntegerField(null=True)
	gender = CharField(max_length=50, choices=gender_choices, null=True)
	email = CharField(max_length=50, null=True)
	mobile = CharField(max_length=50, null=True)
	weightclass = CharField(max_length=50, null=True)
	agecategory = CharField(max_length=50, null=True)
	affiliatedivision = CharField(max_length=50, default = "")

#CLIENTS > Competition
class CompResults(models.Model):
	compdate = DateField(null=True)
	first =  CharField(max_length=50, null=True)
	last = CharField(max_length=50, null=True)
	gender = CharField(max_length=50, choices=gender_choices, null=True)
	age = IntegerField(null=True)
	bodyweight = DecimalField(max_digits=4, decimal_places=1, null=True)
	weightclass = DecimalField(max_digits=4, decimal_places=1, null=True)
	sq1 = DecimalField(max_digits=4, decimal_places=1, null=True)
	sq2 = DecimalField(max_digits=4, decimal_places=1, null=True)
	sq3 = DecimalField(max_digits=4, decimal_places=1, null=True)
	bp1 = DecimalField(max_digits=4, decimal_places=1, null=True)
	bp2 = DecimalField(max_digits=4, decimal_places=1, null=True)
	bp3 = DecimalField(max_digits=4, decimal_places=1, null=True)
	comptotal = DecimalField(max_digits=5, decimal_places=1, null=True)
	wilks = DecimalField(max_digits=5, decimal_places=2, null=True)

#CLIENTS > Payments
class Payments(models.Model):
	paymentdate = DateField(null=True)
	first =  CharField(max_length=50, null=True)
	last = CharField(max_length=50, null=True)
	cyclename = CharField(max_length=50, null=True)
	payplan = IntegerField(choices = payplan_choices, null=True)
	weeks = IntegerField(null=True)
	totaltopay = IntegerField(null=True)
	paid = CharField(max_length=50, choices=paid_choices, null=True)
	method = CharField(max_length=50, choices=method_choices, null=True)

#TRAINING > Cycle Creation (WIDGET)
	first =  CharField(max_length=50, null=True)
	last = CharField(max_length=50, null=True)
	#quick analysis
	se1rm = DecimalField(max_digits=3, decimal_places=2, null=True)
	be1rm = DecimalField(max_digits=3, decimal_places=2, null=True)
	de1rm = DecimalField(max_digits=3, decimal_places=2, null=True)

#TRAINING > Latest Creation
class LatestCycles(models.Model):
	live = CharField(max_length = 3, choices = live_choices, default='no')
	first =  CharField(max_length=50, null=True)
	last = CharField(max_length=50, null=True)
	#cycle details
	cyclename = CharField(max_length=50, null=True)
	startdate = DateField(null=True)
	enddate = DateField(null=True)
	trainingtype = CharField(max_length=50, choices=trainingtype_choices, null=True)
	days = IntegerField(null=True)
	weeks = IntegerField(null=True)
	totaldays = IntegerField(null=True)
	#fatigue protocols >
	sslots = IntegerField(null=True)
	bslots = IntegerField(null=True)
	dslots = IntegerField(null=True)
	totslots = IntegerField(null=True)
	totpct = IntegerField(null=True)
	spctot = IntegerField(null=True)
	bpcttot = IntegerField(null=True)
	dpcttot = IntegerField(null=True)
	# .. > A* fatigue protocols
	smpct = IntegerField(null=True)
	svpct = IntegerField(null=True)
	sspct = IntegerField(null=True)
	bmpct = IntegerField(null=True)
	bv1pct = IntegerField(null=True)
	bv2pct = IntegerField(null=True)
	bs1pct = IntegerField(null=True)
	bs2pct = IntegerField(null=True)
	dmpct = IntegerField(null=True)
	dvpct = IntegerField(null=True)
	dspct = IntegerField(null=True)
	# .. > B* fatigue protocols
	smApct = IntegerField(null=True)
	svApct = IntegerField(null=True)
	ssApct = IntegerField(null=True)
	bmApct = IntegerField(null=True)
	bv1Apct = IntegerField(null=True)
	bv2Apct = IntegerField(null=True)
	bs1Apct = IntegerField(null=True)
	bs2Apct = IntegerField(null=True)
	dmApct = IntegerField(null=True)
	dvApct = IntegerField(null=True)
	dsApct = IntegerField(null=True)
	# .. > A* movements
	smmov = CharField(max_length=100, null=True)
	svmov = CharField(max_length=100, null=True)
	ssmov = CharField(max_length=100, null=True)
	bmmov = CharField(max_length=100, null=True)
	bv1mov = CharField(max_length=100, null=True)
	bv2mov = CharField(max_length=100, null=True)
	bs1mov = CharField(max_length=100, null=True)
	bs2mov = CharField(max_length=100, null=True)
	dmmov = CharField(max_length=100, null=True)
	dvmov = CharField(max_length=100, null=True)
	dsmov = CharField(max_length=100, null=True)
	# .. > B* movements
	smAmov = CharField(max_length=100, null=True)
	svAmov = CharField(max_length=100, null=True)
	ssAmov = CharField(max_length=100, null=True)
	bmAmov = CharField(max_length=100, null=True)
	bv1Amov = CharField(max_length=100, null=True)
	bv2Amov = CharField(max_length=100, null=True)
	bs1Amov = CharField(max_length=100, null=True)
	bs2Amov = CharField(max_length=100, null=True)
	dmAmov = CharField(max_length=100, null=True)
	dvAmov = CharField(max_length=100, null=True)
	dsAmov = CharField(max_length=100, null=True)


#TRAINING > Pending Cycles
#class PendingCycles(models.Model):
	
#TRAINING > Analysis
class AnalysisLatest(models.Model):
	first = CharField(max_length=50, null=True)
	last = CharField(max_length=50, null=True)
	cyclename = CharField(max_length=50, null=True)
	bodyweight = DecimalField(max_digits=4, decimal_places=2, null=True)
	movement = CharField(max_length=100, null=True)
	preve1rm = DecimalField(max_digits=4, decimal_places=2, null=True)
	newe1rm = DecimalField(max_digits=4, decimal_places=2, null=True)
	movetype = CharField(max_length=50, null=True)
	prevratio = DecimalField(max_digits=4, decimal_places=2, null=True)
	newratio = DecimalField(max_digits=4, decimal_places=2, null=True)
	prevfatiguepct = IntegerField(null=True)
	newfatiguepct = IntegerField(null=True)
	analysisreview = IntegerField(null=True)

#CALENDAR (WIDGET)

#RESEARCH > Fatigue Sets Table
#RESEARCH > Fatigue Strength Table
#RESEARCH > Movements
#RESEARCH > Graphs


