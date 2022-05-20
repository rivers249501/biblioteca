from django.shortcuts import render
from .models import User
from rest_framework import viewsets
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny
# from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly
from rest_framework.decorators import action
from book.models import Book
from book.serializers import BookSerializer
from rest_framework.response import Response
from rest_framework import status 


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset =  User.objects.all()
    # permission_classes = [IsAuthenticated]
    
    def get_permissions(self):
        if self.action == "create":
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsOwnerOrReadOnly]
        return [permission() for permission in permission_classes] 
    
    
    @action(detail=True)
    def my_book(self, request,  pk=None):
        queryset = Book.objects.filter(author__id=pk)
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



    # @action(detail=True)
    # def my_cars_on_parking(self, request,  pk=None):
    #     queryset = RackItem.objects.filter(
    #         vehicle__owner__id=pk
    #     ).values_list("vehicle__id", flat=True)
    #     vehicles = Vehicle.objects.filter(
    #         id__in=queryset
    #     )
    #     serializer = VehicleSerializer(vehicles, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK) 
    
    
