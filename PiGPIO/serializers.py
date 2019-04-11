from django.utils.translation import gettext as _
from rest_framework import serializers


class SetPinSerializer(serializers.Serializer):
    pin = serializers.IntegerField()
    mode = serializers.IntegerField()
    state = serializers.IntegerField()


