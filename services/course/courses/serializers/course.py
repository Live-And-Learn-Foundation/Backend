from rest_framework import serializers
from rest_framework.fields import UUIDField
from courses.models import Course, Room, Subject
from courses.serializers.room import RoomSerializer
from courses.serializers.subject import SubjectSerializer


class CourseSerializer(serializers.ModelSerializer):
    room = RoomSerializer(required=False)
    room_id = serializers.PrimaryKeyRelatedField(required=False, write_only=True, queryset=Room.objects.all(),
                                                 pk_field=UUIDField(format='hex'), source='room')
    subject = SubjectSerializer(required=False)
    subject_id = serializers.PrimaryKeyRelatedField(required=False, write_only=True, queryset=Subject.objects.all(),
                                                pk_field=UUIDField(format='hex'), source='subject')

    class Meta:
        model = Course
        fields = [
            "id",
            "subject",
            "subject_id",
            "room",
            "room_id",
            "title",
            "start_date",
            "end_date"
        ]
