from django.urls import path, include, re_path
from django.contrib.auth.models import User, Group
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
from rest_framework.routers import DefaultRouter

from rest_framework_nested import routers

from courses.views import CourseViewSet, RoomViewSet, RoomTypeViewSet

app_name = "courses"

router = routers.SimpleRouter(trailing_slash=False)
router.register(r"courses", CourseViewSet, basename="courses")
router.register(r"rooms", RoomViewSet, basename="rooms")
router.register(r"room_types", RoomTypeViewSet, basename="room_types")

urlpatterns = [
    path(
        r'api/v1/', include(router.urls)
    ),
]
