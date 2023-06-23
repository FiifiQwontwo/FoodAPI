from django.urls import path
from .views import RestaurantList, RestaurantCreateView, MenuList

app_name = 'FDS'

urlpatterns = [
    path('all_restaurants/', RestaurantList.as_view(), name='allrestaurant_api_url'),
    path('create_restaurants/', RestaurantCreateView.as_view(), name='newrestaurant_api_url'),
    path('menulist/', MenuList.as_view(), name='menu_api_url'),
    # path('allusers/', UserList.as_view(), name='allusers_api_url'),

]
