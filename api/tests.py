from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api.user.models import User
from api.bookings.models import Bookings

class UserTest(APITestCase):
  def test_create_user(self):
    """
    Ensure we can create a new user object.
    """
    url = reverse('create-user')
    data = {
      "name": "Max Mustapen",
      "time_zone": "-03:00"
    }
    response = self.client.post(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertEqual(User.objects.count(), 1)
    self.assertEqual(User.objects.get().name, 'Max Mustapen')

class BookingsTest(APITestCase):
  def test_create_booking(self):
    """
    Ensure we can create a new booking object.
    """
    create_user_url = reverse('create-user')
    data = {
      "name": "Max Mustapena",
      "time_zone": "-03:00"
    }
    self.client.post(create_user_url, data, format='json')

    url = reverse('create-booking', kwargs={'mentor': 1})
    data = {
      "date_time":"2019-05-06 07:00:00 +0000",
      "mentor_id": 1,
      "user_id": 1,
      "message": 'message'
    }
    response = self.client.post(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertEqual(Bookings.objects.count(), 1)
    self.assertEqual(Bookings.objects.get().message, 'message')
