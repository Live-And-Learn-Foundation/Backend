from rest_framework import serializers
from rest_framework.fields import UUIDField
from courses.models import Room, RoomType
from courses.serializers.room_type import RoomTypeSerializer


class RoomSerializer(serializers.ModelSerializer):
    room_type = RoomTypeSerializer(required=False)
    room_type_id = serializers.PrimaryKeyRelatedField(required=False, write_only=True, queryset=RoomType.objects.all(),
                                                 pk_field=UUIDField(format='hex'), source='room_type')

    class Meta:
        model = Room
        fields = [
            "id",
            "room_type",
            "room_type_id",
            "title",
            "capacity",
            "location",
        ]
