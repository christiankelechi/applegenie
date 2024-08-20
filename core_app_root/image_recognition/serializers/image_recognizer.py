from rest_framework import serializers
from core_app_root.image_recognition.models import Photo, Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'category']

class PhotoSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Photo
        fields = ['id', 'image', 'tags', 'created_at', 'updated_at']