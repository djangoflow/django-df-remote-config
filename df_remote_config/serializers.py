from rest_framework import serializers


class RemoteConfigSerializer(serializers.Serializer):
    parts = serializers.DictField()
