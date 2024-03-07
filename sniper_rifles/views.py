from django.shortcuts import render

# Create your views here.
from home.models import SniperRiflesPage 

def sniper_rifles_view(request):
    context = {
        "SniperRiflesPage": SniperRiflesPage.objects.all(),
    }
    
    return render(request, "sniper_rifles/sniper_rifles.html", context)