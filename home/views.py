from django.shortcuts import render

from home.models import Car

def home_view(request):
    context = {
        'site_name': 'Cars',
        'cars': Car.objects.all()
    }
    return render(request, "home/home.html", context)

def home_view2(request):
    context = {
        'site_name': 'Cars',
        'cars': Car.objects.all()
    }
    return render(request, "home/home.html", context)