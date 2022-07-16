from rest_framework import serializers
from djoser.serializers import UserSerializer, UserCreateSerializer
from apps.users.models import User
from apps.voices.models import Record, RecordHistory


class CustomUserSerializer(UserSerializer):
    """Custom djoser.serializers.UserSerializer"""
    class Meta(UserSerializer.Meta):
        model = User
        fields = ['id', 'email', 'username', 'first_name', 'last_name', 'avatar_image', 'birth_date', 'sex']


class CustomUserCreateSerializer(UserCreateSerializer):
    """Custom djoser.serializers.UserCreateSerializer"""
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ['email', 'username', 'first_name', 'last_name', 'birth_date', 'password']


class RecordSerializer(serializers.ModelSerializer):
    """Serialize data of Record"""
    class Meta:
        model = Record
        fields = '__all__'


class RecordHistorySerializer(serializers.ModelSerializer):
    """Serialize data of RecordHistory"""
    record = RecordSerializer()

    class Meta:
        model = RecordHistory
        fields = ['id', 'record', 'user', 'created_at']


class VoiceGenerateSerializer(serializers.Serializer):
    """Serialize field for generate voice"""
    text = serializers.CharField(max_length=250)