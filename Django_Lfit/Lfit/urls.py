from . import views
from django.conf.urls import url
from django.contrib.auth.views import login, logout
from .views import CustomView

urlpatterns = [
    url(r'^home$', CustomView.as_view(template_name = 'Lfit/index.html')),
    url(r'^clients$', CustomView.as_view(template_name = 'Lfit/clients.html')),
    url(r'^calendar$', CustomView.as_view(template_name = 'Lfit/calendar.html')),
    url(r'^training$', CustomView.as_view(template_name = 'Lfit/training.html')),
    url(r'^research$', views.research), 
    # url(r'^research$', CustomView.as_view(template_name = 'Lfit/research.html')),
    url(r'^forms_nav$', CustomView.as_view(template_name = 'Lfit/forms_nav.html')),    
    url(r'^login$', login, {'template_name':'login.html'}),

    url(r'^logout$', logout, {'template_name':'logout.html'}),
    url(r'^export$', views.export, name = 'export'),
    # url(r'^matty', views.mattyplot,name = 'matplotlib'),

    url(r'^personalinput$', views.personalinput, name = 'personalinput'),
    url(r'^compresultsinput$', views.compresultsinput, name = 'compresultsinput'),
    url(r'^paymentsinput$', views.paymentsinput, name = 'paymentsinput'),
    url(r'^cyclecreateinput$', views.cyclecreateinput, name = 'cyclecreatinput'),

    url(r'^research2$', views.line_graph),

#====#=====#====# Advanced Form URLs #====#=====#====#=====#

    # url(r'^personalinput$', CustomFormView.as_view(template_name='Lfit/personalinput.html')),
    # url(r'^compresultsinput$', CustomFormView.as_view(template_name='Lfit/compresultsinput.html')),
    # url(r'^paymentsinput$', CustomFormView.as_view(template_name='Lfit/paymentsinput.html')),  
    # url(r'^cyclecreateinput$', CustomFormView.as_view(template_name='Lfit/cyclecreateinput.html')),  
]

