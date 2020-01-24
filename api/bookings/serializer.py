from rest_framework import serializers
from .models import Bookings
from api.openings.models import Openings

class BookingsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Bookings
    fields = ['user_id', 'mentor_id', 'date_time', 'message' ]
  def validate(self, data):
    date_time = data.get('date-time', None)

    opening = Openings.objects.filter(date_time=date_time)
    booking = Bookings.objects.filter(date_time=date_time)
    if not opening.exists():
        raise serializers.ValidationError('This slot is unavailable')
    if booking.exists():
        raise serializers.ValidationError('This slot is has been booked')
    return data[0]
  
  def create(self, validated_data):
    return Bookings.objects.create(**validated_data)
