from rest_framework import (
    mixins,
    viewsets
)

from users import models, serializers

# Create your views here.
class UsersViewSet(mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.CreateModelMixin,
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):
    
    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()