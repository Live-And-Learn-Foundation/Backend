from django.urls import path, include

from rest_framework_nested import routers
from users.views import UserViewSet, RoleViewSet

app_name = "users"

router = routers.SimpleRouter(trailing_slash=False)
router.register(r"", UserViewSet, basename="users")
roleRouter = routers.SimpleRouter(trailing_slash=False)
roleRouter.register(r"", RoleViewSet, basename="roles")

urlpatterns = [
    path(
        r'', include(router.urls)
    ),
    path(
        r'roles/', include(roleRouter.urls)
    ),
]
