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


# class MenuCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MenuItem
#         fields = ('name_of_meal', 'restaurant', 'picture', 'price', 'description')
#
#     def validate(self, data):
#         if data['name_of_meal'] == data['description']:
#             raise serializers.ValidationError(' Name and Description cant be same')
#         else:
#             return value
#
#     def save(self):
#         new_menu = MenuItem(
#             name_of_meal=self.validated_data['name_of_meal'],
#             restaurant=self.validated_data['restaurant'],
#             picture=self.validated_data['picture'],
#             description=self.validated_data['description'],
#             price=self.validated_data['price']
#         )
#         new_menu.save()
#         return new_menu
class MenuCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ('name_of_meal', 'restaurant', 'picture', 'price', 'description')

    def validate(self, data):
        if data['name_of_meal'] == data['description']:
            raise serializers.ValidationError('Name and Description cannot be the same.')
        return data

    def create(self, validated_data):
        return MenuItem.objects.create(**validated_data)


class OrderListSerializer(serializers.ModelSerializer):
    sub_total = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ('customer', 'restaurant', 'food', 'quantity', 'sub_total', 'created_at')

    def get_sub_total(self, obj):
        return obj.sub_total()


class MenuItemSerial(serializers.ModelSerializer):
    food = OrderListSerializer(source='food_orders', many=True)


fields = ('name', 'price', 'order')


class OrderCreateSerializer(serializers.ModelSerializer):
    sub_total = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ('customer', 'restaurant', 'food', 'quantity', 'sub_total', 'created_at')
        read_only_fields = ('sub_total', 'created_at')

    def get_sub_total(self, obj):
        return obj.sub_total()

    def create(self, validated_data):
        quantity = validated_data.get('quantity', 1)
        food = validated_data['food']
        total_amount = food.price * quantity

        order = Order.objects.create(
            customer=validated_data['customer'],
            restaurant=validated_data['restaurant'],
            food=food,
            quantity=quantity,
            total_amount=total_amount
        )

        return order


class DeliveryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = ('id', 'customer', 'order', 'menu_item', 'status', 'created_at',)


class DeliveryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = ('customer', 'order', 'menu_item', 'status')

    def save(self):
        new_delivery = Delivery(
            customer=self.validated_data['customer'],
            order=self.validated_data['order'],
            menu_item=self.validated_data['menu_item'],
            status=self.validated_data['status'],

        )
        new_delivery.save()
        return new_delivery


class MenuListSerializer(serializers.ModelSerializer):
    food_orders = OrderListSerializer(many=True, read_only=True)

    class Meta:
        model = MenuItem
        fields = "__all__"


class RestaurantDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'phone', 'email', 'address')


class DeliveryUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = ['status']

