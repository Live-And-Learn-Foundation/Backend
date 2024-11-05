from rest_framework import serializers
from users.models import UserDetail


class UserDetailSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(required=False)
    class Meta:
        model = UserDetail
        fields = [
            "id",
            "date_of_birth",
            "degree",
            "academic_title",
            "biography"
        ]
        extra_kwargs = {
            "date_of_birth": {"required": False},
            "degree": {"required": False},
            "academic_title": {"required": False},
            "biography": {"required": False},
        }
