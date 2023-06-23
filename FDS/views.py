from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import *
from .serializer import ResturantListSerializer


# Create your views here.
class ResturantList(APIView):
    def get(self, request):
        rest = Restaurant.objects.all()
        serializer = ResturantListSerializer(rest, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
