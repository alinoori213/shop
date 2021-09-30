from django.forms import ModelForm
from .models import Order


class MyForm(ModelForm):
    class Meta:
        model = Order
        fields = ['full_name', 'address1', 'city', 'post_code', 'phone']