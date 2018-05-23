from django.contrib.auth.models import User
from rest_framework import serializers

from simple_post_api_app.models import SimplePost


class SignUpSerializer(serializers.ModelSerializer):

    class Meta:

        model = User
        fields = ("id", "first_name", "last_name", "username", "email", "password")
        write_only_fields = ("password",)
        read_only_fields = ("id",)

    def create(self, validated_data):
        user = User(first_name=validated_data["first_name"],
                    last_name=validated_data["last_name"],
                    username=validated_data["username"],
                    email=validated_data["email"],)

        user.set_password(validated_data["password"])
        user.save()

        return user


# Approach 1 with Serializer
class SimplePostSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    header = serializers.CharField(max_length=200,)
    content = serializers.CharField()
    location = serializers.CharField()
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return SimplePost.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.header = validated_data.get("header", instance.header)
        instance.content = validated_data.get("content", instance.content)
        instance.location = validated_data.get("location", instance.content)

        instance.save()

        return instance


# Approach 2 with ModelSerializer
"""
class SimplePostSerializer(serializers.ModelSerializer):

    class Meta:
        model = SimplePost
        fields = (
            "id",
            "header",
            "content",
            "created",
            "update",
        )
        read_only_fields = (
            "id",
            "created"
        )
"""