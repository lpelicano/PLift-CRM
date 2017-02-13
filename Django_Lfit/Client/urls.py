from . import views
from .views import CustomView, login_client
from django.conf.urls import url
from django.contrib.auth.views import login, logout
from django.contrib.auth.decorators import login_required

urlpatterns = [

    url(r'^dashboard$', CustomView.as_view(template_name = 'Client/dashboard.html'), name="dashboard"),
    url(r'^training$', CustomView.as_view(template_name = 'Client/training.html'), name="training"),
    url(r'^competitions$', CustomView.as_view(template_name = 'Client/competition.html'), name="competitions"),
    url(r'^account$', CustomView.as_view(template_name = 'Client/account.html'), name="account"),   

#====#=====#====# Login URLs #====#=====#====#=====#

    url(r'^login$', login_client, name = "login"),
    url(r'^logout$', logout, {'template_name':'Client/logout.html'}, name="logout"),

    #url(r'^home$', login_required(CustomView.as_view(template_name = 'Lfit/index.html'))),
]