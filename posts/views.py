from django.shortcuts import render
from rest_framework import (
    mixins,
    viewsets
)

from posts import models, serializers

# Create your views here.
class PostsViewSet(mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.CreateModelMixin,
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):
    
    serializer_class = serializers.PostSerializer
    queryset = models.Post.objects.all()

class TagViewSet(mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.CreateModelMixin,
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):
    
    serializer_class = serializers.TagSerializer
    queryset = models.Tag.objects.all()

class CommentViewSet(mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.CreateModelMixin,
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):
    
    serializer_class = serializers.CommentSerializer
    queryset = models.Comment.objects.all()