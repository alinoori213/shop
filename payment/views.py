import json

import stripe
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from orders.forms import MyForm
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView
from orders.models import Order, OrderItem
from basket.basket import Basket
from orders.views import payment_confirmation


def myprint(d):
    for k, v in d.items():

        if isinstance(v, dict):

            myprint(v)
        else:
            print("{0} : {1}".format(k, v))


def order_placed(request):
    basket = Basket(request)

    basket.clear()
    return render(request, 'payment/orderplaced.html')


class Error(TemplateView):
    template_name = 'payment/error.html'


@login_required
def BasketView(request):

    basket = Basket(request)
    total = basket.get_total_price()
    print(type(basket.basket))
    myprint(basket.basket)
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            obj1 = Order()
            obj1.full_name = request.POST.get('full_name')
            obj1.address1 = request.POST.get('address1')
            obj1.address2 = request.POST.get('address1')
            obj1.city = request.POST.get('city')
            obj1.post_code = request.POST.get('post_code')
            obj1.phone = request.POST.get('phone')
            obj1.order_key = '123'
            obj1.total_paid = total
            obj1.user = request.user
            obj1.save()
            return redirect(reverse('payment:order_placed'))

    else:
        form = MyForm()

    return render(request, 'payment/home.html', {'form': form})


