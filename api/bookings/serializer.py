from rest_framework import serializers
from .models import Bookings

class BookingsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Bookings
    fields = ['user_id', 'mentor', 'date_time', ]
