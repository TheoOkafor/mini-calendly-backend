from rest_framework import serializers
from .models import User
from api.bookings.serializer import BookingsSerializer
from api.openings.serializer import OpeningsSerializer

class UserSerializer(serializers.ModelSerializer):
  bookings = BookingsSerializer(source='mentor', many=True, read_only=True)
  calendar = OpeningsSerializer(source='owner', many=True, read_only=True)
  class Meta:
    model = User
    fields = ['name', 'time_zone', 'bookings', 'calendar']
