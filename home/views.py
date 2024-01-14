from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from home.models import Car

def home_view(request):
    context = {
        'site_name': 'Cars',
        'cars': Car.objects.all()
    }
    return render(request, "home/home.html", context)

@csrf_exempt
def order_form_view(request):
    name = request.POST.get('name', None)
    email = request.POST.get('email', None)
    phone_number = request.POST.get('phone_number', None)
    coment = request.POST.get('coment', None)

    print(f'{name}, {email}, {phone_number}, {coment}')

    return HttpResponse(status=200)


def home_view2(request):
    context = {
        'site_name': 'Cars',
        'cars': Car.objects.all()
    }
    return render(request, "home/home.html", context)