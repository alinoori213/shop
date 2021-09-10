from django.shortcuts import render

# Create your views here.


def cart(request):

    context = {}

    return render(request, 'orders/cart.html', context)

def checkout(request):

    context = {}

    return render(request, 'orders/checkout.html', context)
