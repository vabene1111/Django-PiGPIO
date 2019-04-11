from django.utils.translation import gettext as _
from rest_framework import serializers


class SetPinSerializer(serializers.Serializer):
    pin = serializers.IntegerField()
    mode = serializers.IntegerField()
    state = serializers.IntegerField()


class RunProgramSerializer(serializers.Serializer):
    pk = serializers.IntegerField()


class EditProgramSerializer(serializers.Serializer):
    pk = serializers.IntegerField()
    blockly_string = serializers.CharField()
    code = serializers.CharField()
