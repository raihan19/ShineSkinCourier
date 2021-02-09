from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, regProfileForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        reg_form = regProfileForm(request.POST)
        if form.is_valid() and reg_form.is_valid():
            user = form.save()
            reg_user = reg_form.save(commit=False)
            reg_user.user = user
            reg_user.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
        reg_form = regProfileForm()
    return render(request, 'registrationUser/register.html', {'form': form, 'reg_form': reg_form})


@login_required
def profile(request):
    return render(request, 'registrationUser/profile.html')
