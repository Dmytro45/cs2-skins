from django.urls import path
from . import views


urlpatterns = [
    path('', views.rifles_view, name='home'),
]