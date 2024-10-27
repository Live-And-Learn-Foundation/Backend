from django.urls import path, include, re_path
from rest_framework import routers

from .views import Oauth2ViewSet
from .views.jwks import jwks_view

app_name = "oauth"
router = routers.DefaultRouter(trailing_slash=False)

router.register(r"", Oauth2ViewSet, basename="oauth")

urlpatterns = [
    path('jwks/', jwks_view, name='jwks'),
    re_path(r'', include(router.urls)),
]
