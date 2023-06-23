from rest_framework import serializers
from .models import *


class ResturantListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('name', 'phone', 'address', 'email')
