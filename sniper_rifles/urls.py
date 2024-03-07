from django.urls import path
from . import views


urlpatterns = [
    path('', views.sniper_rifles_view, name='home'),
]