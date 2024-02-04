from ssl import AlertDescription
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail

from home.models import RiflesPage, Settings

def home_view(request):
    settings = Settings.load()
    context = {
        "title": settings.title,
        "phone_number": settings.phone_number,
        "RiflesPage": RiflesPage.objects.all()
    }
    
    return render(request, "home/home.html", context)

@csrf_exempt
def order_form_view(request):
    name = request.POST.get('name', None)
    email = request.POST.get('email', None)
    phone_number = request.POST.get('phone_number', None)
    coment = request.POST.get('coment', None)

    print(f'{name}, {email}, {phone_number}, {coment}')

    send_mail(
        "Клієнту",
        "Вітаю! Ми отримали ваше замовлення.....",
        None,
        [email],
        fail_silently=False
    )
    send_mail(
        "Адміну",
        "Вітаю! У вас нове велике замовлення.....",
        None,
        ["dimapetrina2007@gmail.com"],
        fail_silently=False
    )
    send_mail(
        "Помічнику адміна",
        "Вітаю! У вас нове замовлення.....",
        None,
        ["llomudor.msk2009@gmail.com"],
        fail_silently=False
    )

    return HttpResponse(status=200)