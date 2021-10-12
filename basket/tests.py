from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from account.models import UserBase
from store.models import Category, Product


class TestBasketView(TestCase):
    def setUp(self):
        self.myuser = UserBase.objects.create(email='b@gmail.com')
        self.cat1 = Category.objects.create(name='django', slug='django')
        self.cat2 = Category.objects.create(name='django1', slug='django1')
        self.data1 = Product.objects.create(category=self.cat1, title='django beginners', created_by=self.myuser,
                               slug='django-beginners', price='20.00', image='django')
        self.data2 = Product.objects.create(category=self.cat1, title='django intermediate', created_by=self.myuser,
                               slug='django-beginners', price='20.00', image='django')
        self.data3 = Product.objects.create(category=self.cat1, title='django advanced', created_by=self.myuser,
                               slug='django-beginners', price='20.00', image='django')
        self.client.post(
            reverse('basket:basket_add'), {"productid": 1, "productqty": 1, "action": "post"}, xhr=True)
        self.client.post(
            reverse('basket:basket_add'), {"productid": 2, "productqty": 2, "action": "post"}, xhr=True)


    def test_basket_add(self):
        """
        Test adding items to the basket
        """
        response = self.client.post(
            reverse('basket:basket_add'), {"productid": 3, "productqty": 1, "action": "post"}, xhr=True)
        self.assertEqual(response.json(), {'qty': 4})
        response = self.client.post(
            reverse('basket:basket_add'), {"productid": 2, "productqty": 1, "action": "post"}, xhr=True)
        self.assertEqual(response.json(), {'qty': 3})

    def test_basket_delete(self):
        """
        Test deleting items from the basket
        """
        response = self.client.post(
            reverse('basket:basket_delete'), {"productid": 2, "action": "post"}, xhr=True)
        self.assertEqual(response.json(), {'qty': 0, 'subtotal': 0})

    def test_basket_update(self):
        """
        Test updating items from the basket
        """
        response = self.client.post(
            reverse('basket:basket_update'), {"productid": 2, "productqty": 1, "action": "post"}, xhr=True)
        self.assertEqual(response.json(), {'qty': 0, 'subtotal': 0})