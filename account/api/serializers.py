from rest_framework import serializers
from account.models import Discount


class DiscountSerlizer(serializers.ModelSerializer):

     current_user = serializers.SerializerMethodField('_user')

     class Meta:
          model = Discount
          fields = ['discount_code', 'current_user']

     def _user(self, obj):
          request = self.context.get('request', None)
          if request:
               return request.user
