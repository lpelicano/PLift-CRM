from django.contrib import admin

# Register your models here.

from .models import AnalysisLatest, LatestCycles, Payments, CompResults, PersonalInfo 

admin.site.register(AnalysisLatest)
admin.site.register(LatestCycles)
admin.site.register(Payments)
admin.site.register(CompResults)
admin.site.register(PersonalInfo)
