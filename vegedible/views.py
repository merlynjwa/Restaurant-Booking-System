from django.shortcuts import render
from .models import User, Order

# Create your views here.


def home_page(request):
    return render(request, 'vegedible/home_page.html')


def orders(request):
    return render(request, 'vegedible/orders.html')


def create_order(request):
    return render(request, 'vegedible/create_order.html')


def show_orders(request):
    orders = Order.objects.all()
    context = {
        'orders': orders
    }
    return render(request, 'vegedible/show_orders.html', context)
