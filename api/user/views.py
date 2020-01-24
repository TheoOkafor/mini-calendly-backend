from django.shortcuts import render
from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import (
  AllowAny,
)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import (
  CreateAPIView,
  RetrieveAPIView,
)
from .serializer import UserSerializer
from .models import User

LOOKUP_FIELD = 'pk'

class RetrieveUserAPIView(RetrieveAPIView):
  """Retrieve User"""
  permission_classes = (AllowAny,)
  serializer_class = UserSerializer
  queryset = User.objects.all()
  lookup_field = LOOKUP_FIELD

  def perform_update(self, serializer):
    """Update a business webpage."""
    serializer.save(user=self.request.user)

class CreateUserAPIView(CreateAPIView):
  """Create User"""
  permission_classes = (AllowAny,)
  serializer_class = UserSerializer
