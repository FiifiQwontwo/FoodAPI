from django.urls import path
from .views import RestaurantList, RestaurantCreateView, MenuList, MenuCreateView, OrderListView, CreateOrderView

app_name = 'FDS'

urlpatterns = [
    path('all_restaurants/', RestaurantList.as_view(), name='allrestaurant_api_url'),
    path('create_restaurants/', RestaurantCreateView.as_view(), name='newrestaurant_api_url'),
    path('menulist/', MenuList.as_view(), name='menu_api_url'),
    path('createMenu/', MenuCreateView.as_view(), name='newMenu_api_url'),
    path('orders/', OrderListView.as_view(), name='order_api_url'),
    path('neworders/', CreateOrderView.as_view(), name='neworder_api_url'),

]
