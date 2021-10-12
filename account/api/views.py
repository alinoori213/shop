from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from .serializers import DiscountSerlizer
from account.models import Discount, UserBase
from basket.basket import Basket
from rest_framework import generics, status
from rest_framework.response import Response
from datetime import datetime
import pytz
from rest_framework.authentication import SessionAuthentication, BasicAuthentication


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return


class CheckDiscount(generics.GenericAPIView):
    serializer_class = DiscountSerlizer
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    def post(self, request):
        discount_code = request.data['discount_code']
        basket = Basket(request)
        user = request.user
        now = pytz.utc.localize(datetime.now())
        print(user)
        for codes in user.discountCode.all():

            if discount_code == codes.discount_code and now < codes.expire_time and codes.used == False:

                final_price = basket.get_total_price(codes.discount_percent)
                data = {
                    'final_price': final_price,

                }
                codes.used = True
                codes.save()
                return Response(data, status=status.HTTP_200_OK)

        return Response({'error': ('Discount code is not valid')}, status=status.HTTP_400_BAD_REQUEST)



