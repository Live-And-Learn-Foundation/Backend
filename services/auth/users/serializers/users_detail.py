from rest_framework import serializers
from users.models import UserDetail

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetail
        fields = [
            "date_of_birth",
            "degree",
            "academic_title",
            "biography"
        ]