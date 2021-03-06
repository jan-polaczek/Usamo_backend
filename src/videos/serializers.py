from rest_framework import serializers
from .models import *


class VideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Video
        fields = '__all__'

    def to_representation(self, instance):
        category = VideoCategorySerializer(read_only=True)
        category.fields.pop('videos')
        self.fields['category'] = category
        return super(VideoSerializer, self).to_representation(instance)


class VideoCategorySerializer(serializers.ModelSerializer):
    videos = VideoSerializer(many=True, read_only=True)

    class Meta:
        model = VideoCategory
        fields = '__all__'
