from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from PiGPIO.serializers import SetPinSerializer
from gpiozero import LED
from time import sleep


class SetPinView(APIView):
    def post(self, request):
        set_pin(request.data)
        return Response({})


def set_pin(data):
    led = LED(data['pin'])
    led.on()
    sleep(2)
    led.off()
