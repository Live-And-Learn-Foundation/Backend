from django.urls import path, include, re_path
from django.contrib.auth.models import User, Group
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
from rest_framework.routers import DefaultRouter

from rest_framework_nested import routers

from departments.views import TeacherViewSet, TeacherTypeViewSet, TeacherCourseViewSet, TeacherDepartmentViewSet, \
    MajorViewSet, DepartmentViewSet

app_name = "departments"

router = routers.SimpleRouter(trailing_slash=False)
router.register(r"teachers", TeacherViewSet, basename="teachers")
router.register(r"teacher_types", TeacherTypeViewSet, basename="teacher_types")
router.register(r"teacher_courses", TeacherCourseViewSet, basename="teacher_courses")
router.register(r"teacher_departments", TeacherDepartmentViewSet, basename="teacher_departments")
router.register(r"majors", MajorViewSet, basename="majors")
router.register(r"departments", DepartmentViewSet, basename="departments")

urlpatterns = [
    path(
        r'api/v1/', include(router.urls)
    ),
]
