from rest_framework import serializers


class SetPinSerializer(serializers.Serializer):
    pin = serializers.IntegerField()
    mode = serializers.IntegerField()
    state = serializers.IntegerField()
