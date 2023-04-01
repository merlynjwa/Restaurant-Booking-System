from django.shortcuts import render, redirect
from .models import User, Order
from .forms import OrderForm

# Create your views here.


def home_page(request):
    return render(request, 'vegedible/home_page.html')


def orders(request):
    orders = Order.objects.filter(customer=request.user.id)
    context = {
        'orders': orders
    }
    return render(request, 'vegedible/orders.html', context)


def create_order(request):
    if request.method == 'POST':
        order = OrderForm(request.POST)
        if order.is_valid():
            order.instance.customer = request.user
            order.save()
            return redirect('orders')
    order = OrderForm()
    context = {
        'order': order
    }
    return render(request, 'vegedible/create_order.html', context)
