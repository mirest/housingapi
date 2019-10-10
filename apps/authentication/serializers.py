
import jwt
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404 as obj
from rest_framework import serializers

from .models import User


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        write_only=True,
        min_length=6
    )
    email = serializers.EmailField(max_length=255)

    class Meta:
        model = User
        fields = ['email', 'password', 'username']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        if not user:
            raise serializers.ValidationError(
                'A user with this email and password already exists'
            )
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.EmailField(
        max_length=255)
    password = serializers.CharField(
        max_length=128, write_only=True, min_length=6)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        res = super().validate(data)
        user = authenticate(**res)
        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password was not found.'
            )
        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated.'
            )
        return user
