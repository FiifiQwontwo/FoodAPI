from rest_framework import serializers
from .models import *


class RestaurantListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('name', 'phone', 'address', 'email')


class RestaurantCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('name', 'phone', 'address', 'email')

    def save(self):
        new_restaurant = Restaurant(
            name=self.validated_data['name'],
            phone=self.validated_data['phone'],
            address=self.validated_data['address'],
            email=self.validated_data['email']
        )
        new_restaurant.save()
        return new_restaurant


class MenuListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ('name_of_meal', 'restaurant', 'picture', 'price', 'description')


# class RestaurantCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Restaurant
#         fields = ('name', 'phone', 'address', 'email')
#
#     def save(self):
#         new_restaurant = Restaurant(
#             name=self.validated_data['name'],
#             phone=self.validated_data['phone'],
#             address=self.validated_data['address'],
#             email=self.validated_data['email']
#         )
#         new_restaurant.save()
#         return new_restaurant
