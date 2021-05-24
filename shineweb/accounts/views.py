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
from .filters import OrderFilter, MerchantFilter
from .decorators import unauthenticated_user, allowed_users, admin_only, new_allowed_users
import csv
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import OrderForm, deliveryManForm
from django.db.models import Sum
from registrationUser.models import regProfile
from django.template.loader import get_template
import pdfkit
import os, subprocess

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

    neworders = Order.objects.all().order_by('-date_created')[:5]

    context = {'orders': neworders, 'customers': customers,
               'total_orders': total_orders, 'delivered': delivered,
               'pending': pending}

    return render(request, 'accounts/dashboard.html', context)


@login_required(login_url='login')
@new_allowed_users(allowed_roles=['admin'])
def products(request):
    products = Order.objects.all().order_by('-date_created')
    page = request.GET.get('page', 1)
    paginator = Paginator(products, 35)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, 'accounts/products.html', {'products': products})


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def customer(request, pk):
    customer = Order.objects.get(id=pk)
    due = customer.due

    context = {'customer': customer, 'due': due,}
    return render(request, 'accounts/customer.html', context)


@login_required(login_url='login')
@new_allowed_users(allowed_roles=['admin'])
def order_list_admin(request):
    global qorders
    qorders = Order.objects.all().order_by('-date_created')

    orderFilter = OrderFilter(request.GET, queryset=qorders)
    qorders = orderFilter.qs

    page = request.GET.get('page', 1)
    paginator = Paginator(qorders, 35)
    try:
        orders = paginator.page(page)
    except PageNotAnInteger:
        orders = paginator.page(1)
    except EmptyPage:
        orders = paginator.page(paginator.num_pages)

    if request.method == 'POST':
        list_of_id_for_action = request.POST.getlist('for_action')
        list_of_obj = qorders.filter(pk__in=list_of_id_for_action)
        newform = deliveryManForm(request.POST)

        if newform.is_valid():
            list_of_obj.update(assigned_to_deliveryman=newform.cleaned_data['assigned_to_deliveryman'])
            return redirect('dashboard')
    else:
        newform = deliveryManForm()

    context = {'orders': orders, 'filter': orderFilter, 'newform':newform}
    return render(request, 'accounts/order_list_admin.html', context)


@login_required(login_url='login')
@new_allowed_users(allowed_roles=['admin'])
def export_order_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="orders.csv"'

    writer = csv.writer(response)
    writer.writerow(['Merchant username', 'Order ID', 'Customer name',
                     'Customer phone', 'Customer email', 'Product name',
                     'Product price', 'Product category',
                     'Product description', 'Product weight', 'Service charge',
                     'Total sent', 'Received from customer', 'Due',
                     'Date created', 'Status', 'Note', 'Delivery address',
                     'Delivery instruction', 'Delivery area', 'Assigned to deliveryman', 'Sum of received from customer',
                     'Sum of service charge', 'Sum of total sent', 'Sum of due',])

    # orders = Order.objects.all().values_list('merchant__username', 'id', 'customer_name',
    #                                          'customer_phone', 'customer_email', 'product_name',
    #                                          'product_price', 'product_category__category',
    #                                          'product_description', 'product_weight', 'amount',
    #                                          'date_created', 'status', 'note', 'delivery_address',
    #                                          'delivery_instruction', 'delivery_area__delivery_area')
    count = 0
    for order in qorders.values_list('merchant__username', 'id', 'customer_name',
                                    'customer_phone', 'customer_email', 'product_name',
                                    'product_price', 'product_category__category',
                                    'product_description', 'product_weight', 'amount',
                                    'total_received_or_sent', 'received_from_customer', 'due',
                                    'date_created', 'status', 'note', 'delivery_address',
                                    'delivery_instruction', 'delivery_area__delivery_area',
                                     'assigned_to_deliveryman',):
        if count == 0:
            order = list(order)
            order.append(qorders.aggregate(Sum('received_from_customer'))['received_from_customer__sum'])
            order.append(qorders.aggregate(Sum('amount'))['amount__sum'])
            order.append(qorders.aggregate(Sum('total_received_or_sent'))['total_received_or_sent__sum'])
            order.append(qorders.aggregate(Sum('due'))['due__sum'])
            order = tuple(order)
        else:
            order = list(order)
            order.append('NA')
            order.append('NA')
            order.append('NA')
            order.append('NA')
            order = tuple(order)

        writer.writerow(order)
        count += 1

    return response


@login_required(login_url='login')
@new_allowed_users(allowed_roles=['admin'])
def merchant_list_admin(request):
    global morders
    morders = regProfile.objects.all()

    merchantFilter = MerchantFilter(request.GET, queryset=morders)
    morders = merchantFilter.qs

    print(morders)

    page = request.GET.get('page', 1)
    paginator = Paginator(morders, 35)
    try:
        orders = paginator.page(page)
    except PageNotAnInteger:
        orders = paginator.page(1)
    except EmptyPage:
        orders = paginator.page(paginator.num_pages)

    context = {'orders': orders, 'filter': merchantFilter}
    return render(request, 'accounts/merchant_list_admin.html', context)


@login_required(login_url='login')
@new_allowed_users(allowed_roles=['admin'])
def export_merchant_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="merchant.csv"'

    writer = csv.writer(response)
    writer.writerow(['Merchant username', 'Merchant ID', 'Merchant email', 'Merchant name', 'Merchant contact number',
                     'Merchant company name', 'Merchant company address', 'Merchant payment method',
                     'Merchant way of payment',])

    for order in morders.values_list('user__username', 'user_id', 'user__email', 'your_name', 'contact_no',
                                     'company_name', 'company_address', 'payment_method', 'way_of_payment',):

        writer.writerow(order)

    return response


@login_required(login_url='login')
@new_allowed_users(allowed_roles=['admin'])
def transaction_history(request):
    search_term = ''
    if 'search' in request.GET:
        search_term = request.GET['search']
        order_list = Order.objects.all().filter(id=search_term).order_by('-date_created')
    else:
        order_list = Order.objects.all().order_by('-date_created')
    page = request.GET.get('page', 1)
    paginator = Paginator(order_list, 35)
    try:
        t_history = paginator.page(page)
    except PageNotAnInteger:
        t_history = paginator.page(1)
    except EmptyPage:
        t_history = paginator.page(paginator.num_pages)
    return render(request, 'accounts/transaction_history.html', {'t_history': t_history, 'search_term': search_term})


# -------------------(CREATE VIEWS) -------------------
@login_required(login_url='login')
@new_allowed_users(allowed_roles=['admin'])
def createOrder(request):
    action = 'create'
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account/')

    context = {'action': action, 'form': form}
    return render(request, 'accounts/order_form.html', context)


# -------------------(UPDATE VIEWS) -------------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateOrder(request, pk):
    action = 'update'
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/account/customer/' + str(order.id))

    context = {'action': action, 'form': form}
    return render(request, 'accounts/order_form.html', context)


# -------------------(DELETE VIEWS) -------------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        customer_url = '/account/'
        order.delete()
        return redirect(customer_url)

    return render(request, 'accounts/delete_item.html', {'item': order})


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def newcustomer(request, pk):
    newcustomervar = Order.objects.get(id=pk)
    template = get_template('accounts/detail.html')
    html = template.render({'newcustomer': newcustomervar})
    options = {
        'page-size': 'Letter',
        'encoding': "UTF-8",
    }
    # config = pdfkit.configuration(wkhtmltopdf='./bin/wkhtmltopdf-pack')
    WKHTMLTOPDF_CMD = subprocess.Popen(['which', os.environ.get('WKHTMLTOPDF_BINARY', 'wkhtmltopdf')],
                                       stdout=subprocess.PIPE).communicate()[0].strip()
    config = pdfkit.configuration(wkhtmltopdf=WKHTMLTOPDF_CMD)
    pdf = pdfkit.from_string(html, False, options, configuration=config)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename = "order_pdf.pdf"'
    return response
    # context = {'newcustomer': newcustomervar,}
    # return render(request, 'accounts/detail.html', context)

