from django.core.management.base import BaseCommand
from users.models import User, Role
from oauth.models import Application
import random
from django.db.models import Q
from core.settings.base import (
    SECRET_KEY,
    DEFAULT_CLIENT_ID,
    DEFAULT_CLIENT_SECRET,
    SUPER_ADMIN_EMAIL,
    SUPER_ADMIN_PASSWORD,
)
from oauth2_provider.models import AbstractApplication
from django.db import transaction
from django.contrib.auth.hashers import make_password


class Command(BaseCommand):
    help = "Init data"

    def handle(self, *args, **kwargs):
        super_admin_user = self.create_superadmin_account()
        self.create_oauth2_application(user=super_admin_user)
        self.stdout.write(self.style.SUCCESS("Init data successfully"))

    @classmethod
    def create_oauth2_application(cls, user=None):
        # Default page
        default_app = Application.objects.filter(
            Q(client_id=DEFAULT_CLIENT_ID)).exists()
        if not default_app:
            Application.objects.create(
                client_id=DEFAULT_CLIENT_ID,
                client_type="confidential",
                authorization_grant_type="password",
                client_secret=DEFAULT_CLIENT_SECRET,
                name="Bold Voyage Heros Admin",
                algorithm=AbstractApplication.RS256_ALGORITHM,
                scope="__all__",
                skip_authorization=True,
                type=Application.APPLICATION_TYPE_SYSTEM,
                user=user,
            )

    @classmethod
    def create_superadmin_account(cls):
        role, created = Role.objects.get_or_create(
            name="Super Administrator",
            description="Unlimited resources access.",
            scope="__all__",
        )
        super_admin_user = User.objects.filter(email=SUPER_ADMIN_EMAIL).first()
        # Todo: Create office if no ones exist
        if not super_admin_user:
            with transaction.atomic():
                super_admin_user = User.objects.create(
                    email=SUPER_ADMIN_EMAIL,
                    password=make_password(
                        SUPER_ADMIN_PASSWORD, salt=SECRET_KEY),
                    first_name="Super",
                    last_name="Administrator",
                    is_superuser=True,
                    is_staff=True,
                    is_active=True,
                )
                super_admin_user.roles.add(role)
                super_admin_user.save()
        print("Initial super admin created successfully")
        return super_admin_user
