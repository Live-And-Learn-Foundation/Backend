from django.urls import path, include

from rest_framework_nested import routers
from users.views import UserViewSet

app_name = "users"

router = routers.SimpleRouter(trailing_slash=False)
router.register(r"", UserViewSet, basename="users")

urlpatterns = [
    path(
        r'', include(router.urls)
    ),
]
