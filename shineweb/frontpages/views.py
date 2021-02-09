from django.shortcuts import render


def home(request):
    return render(request, 'frontpages/home.html')


def about(request):
    return render(request, 'frontpages/about.html')