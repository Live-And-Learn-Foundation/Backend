from rest_framework import serializers
from documents.models import Thesis


class ThesisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thesis
        fields = [
            "id",
            "user_id",
            "title",
            "description",
            "more_info",
            "submission_date",
        ]
