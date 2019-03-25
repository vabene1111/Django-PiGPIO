from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.mixins import LoginRequiredMixin
from PiGPIO.serializers import SetPinSerializer
from time import sleep

import logging

from PiGPIO.models import Program, ProgramStep

from PiGPIO.helper import raspi

logger = logging.getLogger(__name__)


class SetPinView(APIView, LoginRequiredMixin):
    def post(self, request):
        raspi.set_mode(0)

        raspi.setup_pin(request.data['pin'], request.data['mode'])
        raspi.set_output(request.data['pin'], request.data['state'])
        return Response({})


class RunProgramView(APIView, LoginRequiredMixin):
    def post(self, request):
        raspi.set_mode(0)
        program_id = request.data['program']

        print("Starting Program " + str(program_id))

        # TODO lots of validation for data elements

        step = ProgramStep.objects.earliest('num')

        while True:
            run_step(step)

            try:
                step = ProgramStep.objects.get(num=step.successor_true)
            except ProgramStep.DoesNotExist:
                break

        return Response({})


def run_step(step):
    print('Running Step: ' + str(step))
    if step.type == 'sleep':
        print('Running step sleep')
        sleep(int(step.data))
    elif step.type == 'output':
        print("Running step output")
        raspi.setup_pin(step.pin, 1)
        raspi.set_output(step.pin, int(step.data))


class EditStepView(APIView, LoginRequiredMixin):
    def post(self, request):
        # TODO proper input validation
        if request.data['pk'] != '':
            step = ProgramStep.objects.get(pk=int(request.data['pk']))

            if request.data['num'] != '':
                step.num = int(request.data['num'])
            else:
                step.num = None

            if request.data['pin'] != '':
                step.pin = int(request.data['pin'])
            else:
                step.pin = None

            step.type = request.data['type']
            step.data = request.data['data']

            if request.data['successor_true'] != '':
                step.successor_true = int(request.data['successor_true'])
            else:
                step.successor_true = None

            if request.data['successor_false'] != '':
                step.successor_true = int(request.data['successor_false'])
            else:
                step.successor_false = None

            step.save()

        # TODO proper response
        return Response({})


class NewStepView(APIView, LoginRequiredMixin):
    def post(self, request):
        # TODO proper input validation
        step = ProgramStep()
        step.program_id = request.data['program_pk']
        step.num = request.data['step_num']

        step.save()

        # TODO proper response
        return Response({})


class DeleteStepView(APIView, LoginRequiredMixin):
    def post(self, request):
        # TODO proper input validation
        step = ProgramStep.objects.get(pk=int(request.data['pk']))
        step.delete()

        # TODO proper response
        return Response({})
