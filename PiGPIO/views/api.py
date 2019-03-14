from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from PiGPIO.serializers import SetPinSerializer
from time import sleep

from PiGPIO.helper import raspi


class SetPinView(APIView):
    def post(self, request):
        raspi.set_mode(0)
        raspi.setup_pin(request.data['pin'], request.data['mode'])
        raspi.set_output(request.data['pin'], request.data['state'])
        return Response({})
