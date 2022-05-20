from .models import Book
from rest_framework import serializers
from user.serializers import UserSerializer

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    owner = UserSerializer()

    class Meta:
        model = Book
        fields = "__all__" 

