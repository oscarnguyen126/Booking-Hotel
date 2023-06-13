from .models import User
from rest_framework import serializers
import bcrypt


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password",
            "is_staff",
            "is_active",
        ]


class UserDetailSerializer(serializers.Serializer):
    new_password = serializers.CharField(
        max_length=255, write_only=True, min_length=6, required=False, allow_null=True
    )
    username = serializers.CharField(max_length=255, required=False, allow_null=True)

    def update(self, instance, validated_data):
        if validated_data.get("new_password", None):
            salt = bcrypt.gensalt()
            validated_data["password"] = bcrypt.hashpw(
                validated_data["new_password"].encode("utf-8"), salt
            )

        for data in validated_data:
            setattr(instance, data, validated_data[data])

        instance.save()
        return instance

    def to_representation(self, instance):
        return UserSerializer(instance).to_representation(instance)
