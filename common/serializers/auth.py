from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    remember_me = serializers.BooleanField(default=False)

    class Meta:
        fields = (
            "username",
            "password",
            "remember_me",
        )
