from django.urls import path, include,re_path
from django.contrib.auth.models import User, Group
from rest_framework import generics, permissions, serializers
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
from rest_framework.routers import DefaultRouter
from api_users.views import UserViewSet
app_name = "users"

router = DefaultRouter()
router.register(r"users", UserViewSet, basename="users")

urlpatterns = [
    re_path(
        r"^api/v1/", include(router.urls)
    ),
]
