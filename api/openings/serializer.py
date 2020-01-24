from rest_framework import serializers
from .models import Openings

class OpeningsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Openings
    fields = ['date_time']
