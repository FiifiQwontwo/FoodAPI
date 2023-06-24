from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import *
from .serializer import RestaurantListSerializer, RestaurantCreateSerializer, MenuListSerializer, MenuCreateSerializer, \
    OrderCreateSerializer, OrderListSerializer


# Create your views here.
class RestaurantList(APIView):
    def get(self, request):
        rest = Restaurant.objects.all()
        serializer = RestaurantListSerializer(rest, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RestaurantCreateView(APIView):
    def post(self, request):
        serializer = RestaurantCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MenuList(APIView):
    def get(self, request):
        menu = MenuItem.objects.all()
        serializer = MenuListSerializer(menu, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MenuCreateView(APIView):
    def post(self, request):
        serializer = MenuCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderListView(APIView):

    def get(self, request):
        order = Order.objects.all()
        serializer = OrderListSerializer(order, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


class CreateOrderView(APIView):

    def post(self, request):
        serializer = OrderCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)