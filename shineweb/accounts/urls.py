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
]