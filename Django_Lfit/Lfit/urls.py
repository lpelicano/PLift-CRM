from . import views
from django.conf.urls import url
from django.contrib.auth.views import login, logout


urlpatterns = [
    url(r'^home$', views.index, name = 'home'),
    url(r'^clients$', views.clients, name = 'clients'),
    url(r'^calendar$', views.calendar, name = 'calendar'),
    url(r'^training$', views.training, name = 'training'),
    url(r'^research$', views.research, name = 'research'),
    url(r'^login$', login, {'template_name':'login.html'}),
    url(r'^logout$', logout, {'template_name':'logout.html'}),
    url(r'^export$', views.export, name = 'export'),
    url(r'^input$', views.personalinput, name = 'personalinput'),
]
