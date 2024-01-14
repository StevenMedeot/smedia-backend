from rest_framework import serializers

from posts import models

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        fields = [
            "id",
            "media",
            "description",
            "timestamp",
            "author"
        ]

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tag
        fields = [
            "id",
            "name",
            "posts"
        ]

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = [
            "id",
            "description",
            "timestamp",
            "author",
            "post"
        ]