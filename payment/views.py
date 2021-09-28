import json

import stripe
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from orders.forms import MyForm
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView

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
    total = int(basket.get_total_price())
    print(type(basket.basket))
    myprint(basket.basket)
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')

    else:
        form = MyForm()

    return render(request, 'payment/home.html', {'form': form})


