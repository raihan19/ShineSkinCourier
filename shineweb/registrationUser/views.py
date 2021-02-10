from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, regProfileForm, UserUpdateForm, ProfileUpdateForm
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
            messages.success(request, f'Account created for {username}! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
        reg_form = regProfileForm()
    return render(request, 'registrationUser/register.html', {'form': form, 'reg_form': reg_form})

@login_required
def mapview(request):
    return render(request, 'registrationUser/add_map.html')

@login_required
def profile(request):
    return render(request, 'registrationUser/profile.html')


@login_required
def profileupdate(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        r_form = regProfileForm(request.POST, instance=request.user.regprofile)
        if u_form.is_valid() and p_form.is_valid() and r_form.is_valid():
            u_form.save()
            p_form.save()
            r_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        r_form = regProfileForm(instance=request.user.regprofile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'r_form': r_form,
    }

    return render(request, 'registrationUser/update_profile.html', context)
