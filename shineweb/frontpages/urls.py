from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='frontpages-home'),
    path('about/', views.about, name='frontpages-about'),
]
