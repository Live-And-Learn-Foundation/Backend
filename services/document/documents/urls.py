from django.urls import path, include, re_path
from django.contrib.auth.models import User, Group
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
from rest_framework.routers import DefaultRouter

from rest_framework_nested import routers

from documents.views import ThesisViewSet, SubjectMaterialViewSet

app_name = "courses"

router = routers.SimpleRouter(trailing_slash=False)
router.register(r"thesis", ThesisViewSet, basename="thesis")
router.register(r"subject_materials", SubjectMaterialViewSet, basename="subject_materials")

urlpatterns = [
    path(
        r'api/v1/', include(router.urls)
    ),
]
