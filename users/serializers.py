from .models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password


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

    def create(self, validated_data):
        return User.objects.create(
            email=validated_data["email"],
            username=validated_data["username"],
            password=make_password(validated_data["password"]),
        )


class UserListSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255, required=False, allow_null=True)
    is_staff = serializers.BooleanField()
    is_active = serializers.BooleanField()


class UserUpdateSerializer(serializers.Serializer):
    new_password = serializers.CharField(
        max_length=255, min_length=6, write_only=True, required=False, allow_null=True
    )
    username = serializers.CharField(max_length=255, required=False, allow_null=True)
    is_staff = serializers.BooleanField()
    is_active = serializers.BooleanField()

    def update(self, instance, validated_data):
        if validated_data.get("new_password"):
            instance.password = make_password(validated_data["new_password"])

        instance.username = validated_data["username"]
        instance.is_staff = validated_data["is_staff"]
        instance.is_active = validated_data["is_active"]

        instance.save()
        return instance

    def to_representation(self, instance):
        return UserSerializer(instance).to_representation(instance)
