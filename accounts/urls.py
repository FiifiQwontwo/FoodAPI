from django.urls import path
from .views import RegistrationView, LoginView, LogoutView, UserList

app_name = 'accounts'

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register_api_url'),
    path('login/', LoginView.as_view(), name='login_api_url'),
    path('logout/', LogoutView.as_view(), name='logout_api_url'),
    path('allusers/', UserList.as_view(), name='allusers_api_url'),

]
