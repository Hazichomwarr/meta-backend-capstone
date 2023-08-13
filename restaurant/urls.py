from django.contrib import admin
from django.urls import path, include
from .views import index, MenuItemView, SingleMenuItemView, BookingViewSet


urlpatterns = [
    path("", index, name="home"),
    path("menu/", MenuItemView.as_view()),
    path("menu/<int:pk>", SingleMenuItemView.as_view()),
    # path("restaurant/booking/", include(router.urls)),
]
