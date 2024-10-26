from django.urls import path, include, re_path
from django.contrib.auth.models import User, Group
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
from rest_framework.routers import DefaultRouter

from rest_framework_nested import routers

from students.views import StudentViewSet, StudentCourseViewSet

app_name = "students"

router = routers.SimpleRouter(trailing_slash=False)
router.register(r"students", StudentViewSet, basename="students")
router.register(r"students_courses", StudentCourseViewSet, basename="student_courses")

urlpatterns = [
    path(
        r'api/v1/', include(router.urls)
    ),
]
