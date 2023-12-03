from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_view),
    path('home', views.home_view2),
]