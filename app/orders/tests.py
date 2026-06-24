from decimal import Decimal

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Order


class OrderApiTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='client', password='pass12345')
        self.client.force_authenticate(self.user)

    def test_create_order_keeps_item_when_product_id_is_unknown(self):
        response = self.client.post(
            reverse('order-list'),
            {
                'address': 'Moscow',
                'items': [
                    {
                        'product': 999999,
                        'quantity': 2,
                        'price': '1500.00',
                        'editor_data': {
                            'name': 'Demo suit',
                            'config': {'fabric': 'Wool'},
                        },
                    }
                ],
            },
            format='json',
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.data)
        self.assertEqual(Order.objects.count(), 1)

        order = Order.objects.get()
        item = order.items.get()

        self.assertIsNone(item.product)
        self.assertEqual(order.total, Decimal('3000.00'))
        self.assertIsNone(response.data['items'][0]['product'])
