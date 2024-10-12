from rest_framework import generics, permissions, serializers

from users.models.user import User
from users.models.role import Role
from django.contrib.auth.hashers import make_password

from .role import ShortRoleSerializer


# first we define the serializers
class UserSerializer(serializers.ModelSerializer):
    roles = ShortRoleSerializer(many=True, required=False)
    role_ids = serializers.PrimaryKeyRelatedField(required=False, write_only=True, many=True, allow_null=True,
                                                   allow_empty=True,
                                                   queryset=Role.objects.all(),
                                                   source='roles')

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "is_active",
            "roles"
        ]
        depth = 1


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "password", "first_name", "last_name"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        try:
            user = User.objects.create(**validated_data)
            role, _ = Role.objects.get_or_create(
                name="User",
                description="User role",
                scope="__all__"
            )
            user.roles.add(role)
            user.set_password(validated_data["password"])
            user.is_superuser = False
            user.save()
            return user
        except Exception as e:
            # Call delete method to rollback the user creation
            self.delete(user)
            raise e  # Re-raise the exception to propagate it further

    def delete(self, instance):
        if instance and instance.pk:
            instance.delete()


class ShortUserSerializer(serializers.ModelSerializer):
    roles = ShortRoleSerializer(many=True, required=False)

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "role"
        ]
        depth = 1
