from courses.models import RoomType
from rest_framework import serializers


class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = [
            "id",
            "title",
            "description",
        ]
