from django.shortcuts import render

# Create your views here.


def home_page(request):
    return render(request, 'vegedible/home_page.html')


def create_order(request):
    return render(request, 'vegedible/create_order.html')
