from rest_framework import serializers

from .models import FileModel

class FileSerializer(serializers.ModelSerializer):

    class Meta:
        model = FileModel
        fields = [
            'id',
            'uuid',
            'title',
            'path',
            'updated_at',
            'created_at',
        ]

