from rest_framework import serializers

from users import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = [
            "id",
            "username",
            "display_name",
            "last_login",
        ]
