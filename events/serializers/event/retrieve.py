from rest_framework import serializers


class EventRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
            'id',
            'name',
            'date',
        ]
