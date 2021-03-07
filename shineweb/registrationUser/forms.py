from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import regProfile, Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        return user

class regProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(regProfileForm, self).__init__(*args, **kwargs)
        self.fields['way_of_payment'].widget.attrs['placeholder'] = 'Enter bank account number or bKash merchant number'

    class Meta:
        model = regProfile
        fields = ['your_name', 'contact_no', 'company_name', 'company_address', 'payment_method', 'way_of_payment']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
