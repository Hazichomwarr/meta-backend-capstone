from rest_framework import serializers
from .models import Menu, Booking

# define Serializer class for User model
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = "__all__"
        extra_kwargs = {"inventory": {"max_value": 6}}


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"
        extra_kwargs = {"guests_numb": {"max_value": 6}}
