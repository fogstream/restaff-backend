from rest_framework import serializers


class Padawan(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    surname = serializers.CharField()
    position = serializers.CharField()
    target_position = serializers.CharField(allow_null=True)
