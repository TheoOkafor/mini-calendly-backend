from rest_framework.permissions import (
  AllowAny,
)
from rest_framework.views import APIView
from rest_framework.generics import (
  CreateAPIView,
  RetrieveAPIView
)
from .serializer import BookingsSerializer
from .models import Bookings

class CreateBookingsAPIView(CreateAPIView):
    """Create Booking"""
    permission_classes = (AllowAny,)
    serializer_class = BookingsSerializer
