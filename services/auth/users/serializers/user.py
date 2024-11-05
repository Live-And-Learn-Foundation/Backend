from base.serializers import WritableNestedSerializer
from rest_framework import serializers
from rest_framework.fields import UUIDField
from users.models.role import Role
from users.models.user import User
from users.models.users_detail import UserDetail

from .role import ShortRoleSerializer
from .users_detail import UserDetailSerializer


# first we define the serializers
class UserSerializer(WritableNestedSerializer):
    roles = ShortRoleSerializer(many=True, required=False)
    roles_ids = serializers.PrimaryKeyRelatedField(required=False, write_only=True, many=True, allow_null=True,
                                                   allow_empty=True,
                                                   queryset=Role.objects.all(),
                                                   source='roles')
    user_detail = UserDetailSerializer(required=False)
    user_detail_id = serializers.PrimaryKeyRelatedField(required=False, write_only=True, allow_null=True,
                                                        allow_empty=True,
                                                        queryset=UserDetail.objects.all(),
                                                        pk_field=UUIDField(format='hex'),
                                                        source='user_detail')

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "is_active",
            "roles",
            "roles_ids",
            "user_detail",
            "user_detail_id"
        ]
        depth = 1
        nested_create_fields = ["roles"]
        nested_update_fields = ["roles", "user_detail"]


class CreateUserSerializer(WritableNestedSerializer):
    roles = ShortRoleSerializer(many=True, required=False)
    roles_ids = serializers.PrimaryKeyRelatedField(required=False, write_only=True, many=True, allow_null=True,
                                                   allow_empty=True,
                                                   queryset=Role.objects.all(),
                                                   source='roles')
    nested_create_fields = ["roles"]
    class Meta:
        model = User
        fields = ["id", "email", "password", "first_name", "last_name", "roles", "roles_ids"]
        extra_kwargs = {"password": {"write_only": True, "required": False}}

    def create(self, validated_data):
        roles = validated_data.pop("roles", None)
        try:
            user = User.objects.create(**validated_data)
            if roles:
                user.roles.set(roles)
            user.set_password(validated_data.get("password", validated_data["email"]))
            user.is_superuser = False
            user.is_active = True
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
    user_detail = UserDetailSerializer(required=False)

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "roles",
            "user_detail"
        ]
        depth = 1
