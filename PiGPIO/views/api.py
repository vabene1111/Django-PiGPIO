from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from PiGPIO.serializers import SetPinSerializer
from time import sleep

import logging

from PiGPIO.models import Program, ProgramStep

from PiGPIO.helper import raspi

logger = logging.getLogger(__name__)


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

        print("Program started")

        program = Program.objects.get(pk=program_id)
        program_steps = ProgramStep.objects.filter(program_id=program_id)

        # TODO lots of validation for data elements

        for step in program_steps:
            print("RUN")
            if step.type == '0':
                # do nothing for now
                print("Type 0")
            elif step.type == '1':
                print("Type 1")
                raspi.setup_pin(step.pin, 1)
                raspi.set_output(step.pin, int(step.data))
            elif step.type == '2':
                print("Type 2")
                sleep(int(step.data))

        return Response({})
