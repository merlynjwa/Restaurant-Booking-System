from django.shortcuts import render

# Create your views here.


def home_page(request):
    return render(request, 'restaurant_booking_system/home_page.html')
