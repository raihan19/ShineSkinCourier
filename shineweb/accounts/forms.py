from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *

# class CustomerForm(ModelForm):
# 	class Meta:
# 		model = Order
# 		fields = '__all__'


class OrderForm(forms.ModelForm):
	class Meta:
		model = Order
		fields = '__all__'


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


class deliveryManForm(forms.ModelForm):
	class Meta:
		model = Order
		fields = ['assigned_to_deliveryman']
