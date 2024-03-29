from django.shortcuts import render
from .models import Book
from rest_framework import viewsets
from .serializers import BookSerializer
from .permissions import IsOwnerOrReadOnlyBook
from rest_framework.permissions import  IsAdminUser
# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework import filters 


# Create your views here.
class BookViewset(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer 

    def get_permissions(self):
        if self.action == "create":
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsOwnerOrReadOnlyBook]
        return [permission() for permission in permission_classes] 
    
    # def get_queryset(self):
    #     queryset = Vehicle.objects.filter(color)
    #     color = self.request.query_params.get('color', None)
    #     if color is not None:
    #         queryset = queryset.filter(color=color)
    #     return queryset
    # filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    # filterset_fields = ['title', 'isbn']
    # search_fields = ['title']