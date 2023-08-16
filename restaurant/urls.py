from django.contrib import admin
from django.urls import path, include
from .views import index, MenuItemView, SingleMenuItemView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("", index, name="home"),
    path("menu/", MenuItemView.as_view()),
    path("menu/<int:pk>", SingleMenuItemView.as_view()),
    # path("restaurant/booking/", include(router.urls)),
    path("api-token-auth/", obtain_auth_token),
]
