from rest_framework import serializers

from ..users import UserCreateSerializer


class EventUserCreateSerializer(serializers.ModelSerializer):
    user = UserCreateSerializer()

    class Meta:
        fields = [
            'event',
            'user',
        ]
