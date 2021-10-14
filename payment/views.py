from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from orders.forms import MyForm
from django.views.generic.base import TemplateView
from orders.models import Order, OrderItem
from store.models import Product
from basket.basket import Basket
from account.models import Discount



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
    if 'discount_code' in request.session.keys():
        discount = request.session['discount_code']
        print(discount)
        total = basket.get_total_price(discount=discount)
        del request.session['discount_code']
    else:
        total = basket.get_total_price(discount=0)
    if request.method == 'POST':
        form = MyForm(request.POST)
        if len(basket.basket) != 0:
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
                obj1.billing_status = True
                obj1.save()
                print(total)
                for i in basket.basket:
                    temp_product_id = i
                    prd = Product.objects.get(id=i)
                    temp_product_price = basket.basket[i]['price']
                    temp_product_qty = basket.basket[i]['qty']
                    obj = OrderItem.objects.create(order=obj1, product=prd, price=temp_product_price, quantity=temp_product_qty)
                    obj.save()

                return redirect(reverse('payment:order_placed'))

    else:
        form = MyForm()

    return render(request, 'payment/home.html', {'form': form, 'total': total})


