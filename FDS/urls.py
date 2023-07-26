from django.urls import path
from .views import RestaurantList, RestaurantCreateView, UpdateDeliveryView,  MenuList, MenuCreateView, OrderListView, CreateOrderView,DeliveryListView, CreateDeliveryView, RestaurantDetailAPI

app_name = 'FDS'

urlpatterns = [
    path('all_restaurants/', RestaurantList.as_view(), name='allrestaurant_api_url'),
    path('all_restaurants/<int:pk>/', RestaurantDetailAPI.as_view(), name='Detailed_api_url'),
    path('all_restaurants/<int:pk>/', RestaurantDetailAPI.as_view(), name='Delete_api_url'),
    path('create_restaurants/', RestaurantCreateView.as_view(), name='newrestaurant_api_url'),
    path('menulist/', MenuList.as_view(), name='menu_api_url'),
    path('createMenu/', MenuCreateView.as_view(), name='newMenu_api_url'),
    path('orders/', OrderListView.as_view(), name='order_api_url'),
    path('neworders/', CreateOrderView.as_view(), name='neworder_api_url'),
    path('deliveries/', DeliveryListView.as_view(), name='deliveries_api_url'),
    path('newdelivery/', CreateDeliveryView.as_view(), name='newdelivery_api_url'),
    path('newdelivery/<int:pk>', UpdateDeliveryView.as_view(), name='update existing delivery_api_url'),

]
