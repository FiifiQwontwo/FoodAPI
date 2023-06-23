from .serializers import AccountSerializer,  AccountRegistrationSerializer
from .models import Account
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response


class RegistrationView(APIView):
    def post(self, request):
        serializer = AccountRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({'msg': 'Successfully Logged out'}, status=status.HTTP_200_OK)


class LoginView(APIView):
    def post(self, request):
        if 'email' not in request.data or 'password' not in request.data:
            return Response({'msg': 'Credentials missing'}, status=status.HTTP_400_BAD_REQUEST)
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return Response({'msg': 'Login Success'}, status=status.HTTP_200_OK)
        return Response({'msg': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class UserList(APIView):
    def get(self, request):
        user = Account.objects.all()
        serializer = AccountSerializer(user, many=True)
        return Response(serializer.data,  status=status.HTTP_200_OK)
