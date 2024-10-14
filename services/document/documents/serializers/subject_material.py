from rest_framework import serializers
from documents.models import SubjectMaterial


class SubjectMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectMaterial
        fields = [
            "id",
            "subject_id",
            "title",
            "file_path",
            "description",
        ]
