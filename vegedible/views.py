from django.shortcuts import render, redirect, get_object_or_404
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


def edit_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if order.customer != request.user:
        return render(request, 'vegedible/edit_order_not_authorised.html')
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('orders')
    form = OrderForm(instance=order)
    context = {
        'form': form
    }
    return render(request, 'vegedible/edit_order.html', context)
