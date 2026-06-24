from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import MeasurementRequest


class MeasurementRequestApiTests(APITestCase):
    def test_guest_can_create_measurement_request(self):
        response = self.client.post(
            reverse('measurement-request-list-create'),
            {
                'full_name': 'Иван Иванов',
                'phone': '+7 999 123-45-67',
                'email': 'ivan@example.com',
                'preferred_time': 'После 18:00',
                'wishes': 'Нужен деловой костюм на осень',
            },
            format='json',
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(MeasurementRequest.objects.count(), 1)

    def test_staff_can_view_all_measurement_requests(self):
        staff = User.objects.create_user(username='manager', password='pass12345', is_staff=True)
        MeasurementRequest.objects.create(full_name='Петр', phone='+7 900 000-00-00')

        self.client.force_authenticate(staff)
        response = self.client.get(reverse('measurement-request-list-create'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

