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
import csv
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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
    products = Order.objects.all()

    return render(request, 'accounts/products.html', {'products': products})


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def customer(request, pk):
    global qorders
    customer = Order.objects.get(id=pk)
    qorders = Order.objects.all()
    total_orders = qorders.count()

    orderFilter = OrderFilter(request.GET, queryset=qorders)
    qorders = orderFilter.qs

    context = {'customer': customer, 'orders': qorders, 'total_orders': total_orders,
               'filter': orderFilter}
    return render(request, 'accounts/customer.html', context)


@login_required(login_url='login')
@new_allowed_users(allowed_roles=['admin'])
def export_order_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="orders.csv"'

    writer = csv.writer(response)
    writer.writerow(['Merchant', 'Order ID', 'Customer name',
                     'Customer phone', 'Customer email', 'Product name',
                     'Product price', 'Product category',
                     'Product description', 'Product weight', 'Amount',
                     'Date created', 'Status', 'Note', 'Delivery address',
                     'Delivery instruction', 'Delivery area'])

    # orders = Order.objects.all().values_list('merchant__username', 'id', 'customer_name',
    #                                          'customer_phone', 'customer_email', 'product_name',
    #                                          'product_price', 'product_category__category',
    #                                          'product_description', 'product_weight', 'amount',
    #                                          'date_created', 'status', 'note', 'delivery_address',
    #                                          'delivery_instruction', 'delivery_area__delivery_area')
    for order in qorders.values_list('merchant__username', 'id', 'customer_name',
                                    'customer_phone', 'customer_email', 'product_name',
                                    'product_price', 'product_category__category',
                                    'product_description', 'product_weight', 'amount',
                                    'date_created', 'status', 'note', 'delivery_address',
                                    'delivery_instruction', 'delivery_area__delivery_area'):
        writer.writerow(order)

    return response


@login_required(login_url='login')
@new_allowed_users(allowed_roles=['admin'])
def transaction_history(request):
    search_term = ''
    if 'search' in request.GET:
        search_term = request.GET['search']
        t_history = Order.objects.all().filter(id=search_term)
    else:
        t_history = Order.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(t_history, 5)
    try:
        t_history = paginator.page(page)
    except PageNotAnInteger:
        t_history = paginator.page(1)
    except EmptyPage:
        t_history = paginator.page(paginator.num_pages)
    return render(request, 'accounts/transaction_history.html', {'t_history': t_history, 'search_term': search_term})


