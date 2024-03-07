from django.shortcuts import render

# Create your views here.
from home.models import RiflesPage

def rifles_view(request):
    context = {
        "RiflesPage": RiflesPage.objects.all(),
    }
    
    return render(request, "rifles/rifles.html", context)