from rest_framework.generics import UpdateAPIView
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import *
from .serializer import RestaurantListSerializer, RestaurantCreateSerializer, MenuListSerializer, MenuCreateSerializer, \
    OrderCreateSerializer, OrderListSerializer, DeliveryCreateSerializer, DeliveryListSerializer, \
    RestaurantDetailSerializer, DeliveryUpdateSerializer
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


# Create your views here.
class RestaurantList(APIView):
    @swagger_auto_schema(
        operation_description="List Restaurant",
        responses={
            200: openapi.Response(
                description="OK",
                schema=openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            'name': openapi.Schema(type=openapi.TYPE_STRING, description='name of restaurant'),
                            'phone': openapi.Schema(type=openapi.TYPE_NUMBER, description='Phone of restaurant'),
                            'email': openapi.Schema(type=openapi.TYPE_STRING, description='email of restaurant'),
                            'address': openapi.Schema(type=openapi.TYPE_STRING, description='address of restaurant'),
                        },
                    ),
                ),
            ),
            400: 'Bad Request',
            401: 'Unauthorized',
            403: 'Forbidden',
            500: 'Internal Server Error',
        }
    )
    def get(self, request):
        rest = Restaurant.objects.all()
        serializer = RestaurantListSerializer(rest, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RestaurantCreateView(APIView):

    @swagger_auto_schema(
        operation_description="Create a new Restaurant",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['name', 'phone', 'email', 'address'],
            properties={
                'name': openapi.Schema(type=openapi.TYPE_STRING, description='name of the restaurant'),
                'phone': openapi.Schema(type=openapi.TYPE_STRING, description='phone number of the restaurant'),
                'email': openapi.Schema(type=openapi.TYPE_STRING, description='email of the restaurant'),
                'address': openapi.Schema(type=openapi.TYPE_STRING, description='address of the restaurant'),

            }
        ),
        responses={
            201: 'Created',
            400: 'Bad Request',
            401: 'Unauthorized',
            403: 'Forbidden',
            500: 'Internal Server Error',
        }
    )
    def post(self, request):
        serializer = RestaurantCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MenuList(APIView):
    @swagger_auto_schema(
        operation_description="List Menu",
        responses={
            200: openapi.Response(
                description="OK",
                schema=openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            'restaurant': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID of the restaurant'),
                            'name_of_meal': openapi.Schema(type=openapi.TYPE_STRING, description='name of the food'),
                            'picture': openapi.Schema(type=openapi.TYPE_FILE, description='picture of the food'),
                            'description': openapi.Schema(type=openapi.TYPE_STRING, description='details of the food'),
                            'price': openapi.Schema(type=openapi.TYPE_NUMBER, description='price of the food'),
                        },
                    ),
                ),
            ),
            400: 'Bad Request',
            401: 'Unauthorized',
            403: 'Forbidden',
            500: 'Internal Server Error',
        }
    )
    def get(self, request):
        menu = MenuItem.objects.all()
        serializer = MenuListSerializer(menu, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MenuCreateView(APIView):
    @swagger_auto_schema(
        operation_description="Create a new Menu",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['restaurant', 'name_of_meal', 'picture', 'description', 'price'],
            properties={
                'restaurant': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID of the restaurant'),
                'name_of_meal': openapi.Schema(type=openapi.TYPE_STRING, description='name of  food '),
                'picture': openapi.Schema(type=openapi.TYPE_FILE, description='Picture of the food '),
                'description': openapi.Schema(type=openapi.TYPE_STRING, description='description of the food '),
                'price': openapi.Schema(type=openapi.TYPE_NUMBER, description='Price of the food '),
            }
        ),
        responses={
            201: 'Created',
            400: 'Bad Request',
            401: 'Unauthorized',
            403: 'Forbidden',
            500: 'Internal Server Error',
        }
    )
    def post(self, request):
        serializer = MenuCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderListView(APIView):
    @swagger_auto_schema(
        operation_description="List Orders",
        responses={
            200: openapi.Response(
                description="OK",
                schema=openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            'customer': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID of the customer'),
                            'restaurant': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID of the restaurant'),
                            'food': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID of the menu item'),
                            'quantity': openapi.Schema(type=openapi.TYPE_INTEGER, description='quantity ordered'),
                            'total_amount': openapi.Schema(type=openapi.TYPE_INTEGER, description='order total'),
                        },
                    ),
                ),
            ),
            400: 'Bad Request',
            401: 'Unauthorized',
            403: 'Forbidden',
            500: 'Internal Server Error',
        }
    )
    def get(self, request):
        order = Order.objects.all()
        serializer = OrderListSerializer(order, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CreateOrderView(APIView):
    @swagger_auto_schema(
        operation_description="Create a new order",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['customer', 'restaurant', 'food', 'quantity'],
            properties={
                'customer': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID of the customer'),
                'restaurant': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID of the restaurant'),
                'food': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID of the food item'),
                'quantity': openapi.Schema(type=openapi.TYPE_INTEGER, description='Quantity of the food item'),
            }
        ),
        responses={
            201: 'Created',
            400: 'Bad Request',
            401: 'Unauthorized',
            403: 'Forbidden',
            500: 'Internal Server Error',
        }
    )
    def post(self, request):
        serializer = OrderCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeliveryListView(APIView):
    @swagger_auto_schema(
        operation_description="List deliveries",
        responses={
            200: openapi.Response(
                description="OK  delivery List",
                schema=openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            'customer': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID of the customer'),
                            'order': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID of the order'),
                            'menu_item': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID of the menu item'),
                            'status': openapi.Schema(type=openapi.TYPE_STRING, description='Delivery status'),
                            'created_at': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME,
                                                         description='Date and time of creation'),
                        },
                    ),
                ),
            ),
            400: 'Bad Request',
            401: 'Unauthorized',
            403: 'Forbidden',
            500: 'Internal Server Error',
        }
    )
    def get(self, request):
        delivery = Delivery.objects.all()
        serializer = DeliveryListSerializer(delivery, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CreateDeliveryView(APIView):
    @swagger_auto_schema(
        operation_description="Create a new delivery",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['order', 'menu_item', 'customer', 'status'],
            properties={
                'customer': openapi.Schema(type=openapi.TYPE_INTEGER),
                'order': openapi.Schema(type=openapi.TYPE_INTEGER),
                'menu_item': openapi.Schema(type=openapi.TYPE_INTEGER),
                'status': openapi.Schema(type=openapi.TYPE_STRING),
                'created_at': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME),
            }
        ),
        responses={
            201: 'Created a  New Delivery',
            400: 'Bad Request',
            401: 'Unauthorized',
            403: 'Forbidden',
            500: 'Internal Server Error',
        }
    )
    def post(self, request):
        serializer = DeliveryCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RestaurantDetailAPI(APIView):
    @swagger_auto_schema(

        operation_description="Get Restaurant Details",
        responses={
            200: RestaurantDetailSerializer(),
            404: "Restaurant not found",
        }
    )
    def get(self, request, pk):
        try:
            restaurant = Restaurant.objects.get(pk=pk)
            serializer = RestaurantDetailSerializer(restaurant)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Restaurant.DoesNotExist:
            return Response({'Error': 'Restaurant not found'}, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        operation_description="Delete Restaurant",
        responses={
            204: "Restaurant Deleted",
            404: "Restaurant Not Found",
        }
    )
    def delete(self, request, pk):
        try:
            restaurant = Restaurant.objects.get(pk=pk)
        except Restaurant.DoesNotExist:
            return Response({'Error': 'Restaurant not found'}, status=status.HTTP_404_NOT_FOUND)
        restaurant.delete()
        return Response({'message': 'Restaurant deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


 # Create the API view for updating the delivery
class UpdateDeliveryView(UpdateAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliveryUpdateSerializer

    @swagger_auto_schema(
        operation_description="Update an existing delivery",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['status'],
            properties={
                'status': openapi.Schema(type=openapi.TYPE_STRING),
            }
        ),
        responses={
            200: 'Delivery updated successfully',
            400: 'Bad Request',
            401: 'Unauthorized',
            403: 'Forbidden',
            404: 'Delivery not found',
            500: 'Internal Server Error',
        }
    )
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
