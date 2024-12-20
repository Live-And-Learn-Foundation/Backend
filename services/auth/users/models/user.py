# Create your models here.
import uuid

from base.models.timestamped import TimeStampedModel
from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone
from oauth.managers.user_manager import UserManager

from .role import Role
from .users_detail import UserDetail

# from common.constants.gender import Genders

AUTH_PROVIDERS = {'facebook': 'facebook', 'google': 'google',
                  'twitter': 'twitter', 'email': 'email'}


class User(TimeStampedModel, AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    password = models.CharField(verbose_name="password", max_length=255)
    email = models.EmailField(max_length=255, unique=True, null=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(
        "staff status",
        default=False,
        help_text="Designates whether the user can log into this admin site.",
    )
    roles = models.ManyToManyField(Role, related_name="users", null=True)
    user_detail = models.ForeignKey(UserDetail, on_delete=models.CASCADE, related_name='users', null=True, blank=True)
    date_joined = models.DateTimeField(default=timezone.now)
    auth_provider = models.CharField(
        max_length=255, blank=False,
        null=False, default=AUTH_PROVIDERS.get('email'))
    USERNAME_FIELD = "email"  # username
    objects = UserManager()

    class Meta:
        db_table = "users"

    def __str__(self):
        return str(self.id)

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def set_password(self, raw_password):
        self.password = make_password(
            password=raw_password, salt=settings.SECRET_KEY)
        self._password = raw_password

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
