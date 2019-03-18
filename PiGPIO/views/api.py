from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from PiGPIO.serializers import SetPinSerializer
from time import sleep

from PiGPIO.models import Program, ProgramStep

from PiGPIO.helper import raspi


class SetPinView(APIView):
    def post(self, request):
        raspi.set_mode(0)
        raspi.setup_pin(request.data['pin'], request.data['mode'])
        raspi.set_output(request.data['pin'], request.data['state'])
        return Response({})


class RunProgramView(APIView):
    def post(self, request):
        raspi.set_mode(0)
        program_id = request.data['program']

        program = Program.objects.get(pk=program_id)
        program_steps = ProgramStep.objects.filter(pk=program_id)

        for step in program_steps:
            if step.type == 0:
                # do nothing for now
                print("BlaBla")
            elif step.type == 1:
                raspi.setup_pin(step.pin, 1)
                raspi.set_output(step.pin, step.data)
            elif step.type == 2:
                sleep(step.data)

        return Response({})
