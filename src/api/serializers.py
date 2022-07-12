from rest_framework import serializers
from djoser.serializers import UserSerializer, UserCreateSerializer
from users.models import User


class CustomUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = User
        fields = ['id', 'email', 'username', 'first_name', 'last_name', 'avatar_image', 'birth_date', 'sex']


class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ['email', 'username', 'first_name', 'last_name', 'birth_date', 'password']
