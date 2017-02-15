from django.contrib import admin

# Register your models here.

from .models import (AnalysisLatest, 
										 CycleCreate, 
										 Payments, 
										 CompResults, 
										 PersonalInfo,
										 UserProfile,
										 )


admin.site.register(AnalysisLatest)
admin.site.register(CycleCreate)
admin.site.register(Payments)
admin.site.register(CompResults)
admin.site.register(PersonalInfo)
admin.site.register(UserProfile)
