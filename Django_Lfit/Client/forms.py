from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class CustomLoginForm(AuthenticationForm):
	class Meta: 
		model = User


class ImageUploadForm(forms.Form): 
	image = forms.ImageField()