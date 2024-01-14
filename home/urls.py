from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_view),
    path('order-form', views.order_form_view, name='order-form'),
    path('home', views.home_view2),
]