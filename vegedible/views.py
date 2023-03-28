from django.shortcuts import render
from .models import Customer, Order

# Create your views here.


def home_page(request):
    return render(request, 'vegedible/home_page.html')


def create_order(request):
    return render(request, 'vegedible/create_order.html')


def show_orders(request):
    return render(request, 'vegedible/show_orders.html')
