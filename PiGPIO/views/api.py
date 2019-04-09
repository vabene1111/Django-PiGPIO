from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.mixins import LoginRequiredMixin

from PiGPIO.interpreter import lex, parse
from PiGPIO.serializers import SetPinSerializer
from time import sleep

import logging

from PiGPIO.models import Program, ProgramStep, ProgramLog

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
        program_id = request.data['pk']

        print("Starting Program " + str(program_id))

        program = Program.objects.get(pk=program_id)
        program.running = True
        program.save()

        ProgramLog.objects.all().delete()

        step = ProgramStep.objects.filter(program_id=program_id).earliest('num')

        env = {'dont_use_this_name': True}

        while True:
            program = Program.objects.get(pk=step.program_id)

            if not program.running:  # TODO check why not working on pi
                if program.logging:
                    log = ProgramLog()
                    log.info = 'Program Terminated'
                    log.save()
                break

            if program.logging:
                log = ProgramLog()
                log.step = step
                log.save()

            env = run_step(step, env)

            try:
                if env['dont_use_this_name'] is True:
                    step = ProgramStep.objects.get(num=step.successor_true, program_id=program_id)
                else:
                    step = ProgramStep.objects.get(num=step.successor_false, program_id=program_id)
                    env['dont_use_this_name'] = True
            except ProgramStep.DoesNotExist:
                if program.logging:
                    log = ProgramLog()
                    log.info = 'Program Ended'
                    log.save()
                break

        log = pretty_print_log()
        return Response({'log': log})


def pretty_print_log():
    output = ""

    logs = ProgramLog.objects.all()

    for log in logs:
        if log.info is not '':
            output = output + str(log.created_at) + ' - ' + log.info + '\n'
        else:
            output = output + str(log) + '\n'

    return output


def run_interpreter(code, env):
    tokens = lex(code)
    result = parse(tokens)

    if not result:
        print('Praser failed')

    ast = result.value
    ast.eval(env)
    return env


def run_step(step, env):
    print('Running Step: ' + str(step))
    if step.type == 'sleep':
        print('Running step sleep')
        sleep(int(step.data))
    elif step.type == 'output':
        print("Running step output")
        raspi.setup_pin(step.pin, 1)
        raspi.set_output(step.pin, int(step.data))
    elif step.type == 'variable':
        print("Variable assignment ", step.data, env)
        run_interpreter(step.data, env)
        print("After env: ", env)
    elif step.type == 'condition':
        print("Condition")
        code = "if " + step.data + " then dont_use_this_name = True else dont_use_this_name = False end"
        print(code, env)
        run_interpreter(code, env)
        print("After env: ", env)

    return env


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
                step.successor_false = int(request.data['successor_false'])
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


class StopProgramView(APIView, LoginRequiredMixin):
    def post(self, request):
        # TODO proper input validation
        program = Program.objects.get(pk=int(request.data['pk']))

        program.running = False

        program.save()

        # TODO proper response
        return Response({})
