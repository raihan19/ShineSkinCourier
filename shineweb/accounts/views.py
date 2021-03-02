from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

# Create your views here.
from .models import *
# from .forms import OrderForm, CreateUserForm, CustomerForm
from .filters import OrderFilter
from .decorators import unauthenticated_user, allowed_users, admin_only, new_allowed_users


# @unauthenticated_user
# def registerPage(request):
#     form = CreateUserForm()
#     if request.method == 'POST':
#         form = CreateUserForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             username = form.cleaned_data.get('username')
#
#             messages.success(request, 'Account was created for ' + username)
#
#             return redirect('login')
#
#     context = {'form': form}
#     return render(request, 'accounts/register.html', context)


@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('adminlogin')


@login_required(login_url='login')
@admin_only
def home(request):
    orders = Order.objects.all()
    customers = Order.objects.all()

    # total_customers = customers.count()

    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {'orders': orders, 'customers': customers,
               'total_orders': total_orders, 'delivered': delivered,
               'pending': pending}

    return render(request, 'accounts/dashboard.html', context)


@login_required(login_url='login')
@new_allowed_users(allowed_roles=['admin'])
def products(request):
    products = Product.objects.all()

    return render(request, 'accounts/products.html', {'products': products})


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def customer(request, pk):
    customer = Order.objects.get(id=pk)
    orders = Order.objects.all()
    total_orders = orders.count()

    orderFilter = OrderFilter(request.GET, queryset=orders)
    orders = orderFilter.qs

    context = {'customer': customer, 'orders': orders, 'total_orders': total_orders,
               'filter': orderFilter}
    return render(request, 'accounts/customer.html', context)