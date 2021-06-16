from rest_framework import serializers
from .models import VideoDetail, ApiKey


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoDetail
        fields = '__all__'


class APIKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiKey
        fields = '__all__'
