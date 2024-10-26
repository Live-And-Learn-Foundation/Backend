from rest_framework import serializers
from departments.models import TeacherType


class TeacherTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherType
        fields = [
            "id",
            "name",
        ]
