from django.urls import path, include, re_path
from django.contrib.auth.models import User, Group
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
from rest_framework.routers import DefaultRouter

from rest_framework_nested import routers
from users.views import UserViewSet

app_name = "users"

router = routers.SimpleRouter(trailing_slash=False)
router.register(r"", UserViewSet, basename="users")

urlpatterns = [
    path(
        r'api/v1/users/', include(router.urls)
    ),
]
