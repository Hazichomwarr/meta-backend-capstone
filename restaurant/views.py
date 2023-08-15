from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from .models import Booking, Menu
from .serializers import BookingSerializer, MenuItemSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated


# Create your views here.
def index(request):
    return render(request, "index.html", {})


class MenuItemView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer


# class BookingView(generics.ListCreateAPIView):
#     queryset = Booking.objects.all()
#     serializer_class = BookingSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
