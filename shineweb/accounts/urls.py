from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name="dashboard"),
    path('products/', views.products, name="products"),
    path('customer/<str:pk>/', views.customer, name="customer"),
    # path('register/', views.registerPage, name="register"),
    path('adminlogin/', views.loginPage, name="adminlogin"),
    path('adminlogout/', views.logoutUser, name="adminlogout"),
    path('export/csv/', views.export_order_csv, name='export_orders_csv'),
    path('export/csv/merchant/', views.export_merchant_csv, name='export_merchants_csv'),
    path('transaction_history/', views.transaction_history, name="transaction-history"),
    path('orderlistadmin/', views.order_list_admin, name="order-list-admin"),
    path('merchantlistadmin/', views.merchant_list_admin, name="merchant-list-admin"),
    #------------ (CREATE URLS) ------------
    path('create_order/', views.createOrder, name="create_order"),

    #------------ (UPDATE URLS) ------------
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),


    #------------ (UPDATE URLS) ------------
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),
]
