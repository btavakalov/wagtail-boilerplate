from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'url',
            'email',
            'is_active',
            'date_joined',
        )


class UserCreateSerializer(UserSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'url',
            'email',
            'is_active',
        )


class UserUpdateSerializer(UserCreateSerializer):
    pass
