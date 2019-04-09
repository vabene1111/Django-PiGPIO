import sys

from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.response import Response
from rest_framework.views import APIView

from PiGPIO.helper import raspi, UndefinedPinException, OutputNotSupportedException
from PiGPIO.models import Program


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
        program = Program.objects.get(pk=program_id)

        program.running = False

        program.save()

        try:
            exec(program.code)
        except UndefinedPinException:
            return Response({'error': 'ERROR: Trying to set status of undefined pin'})  # TODO localize
        except OutputNotSupportedException as e:
            return Response({'error': 'ERROR: Trying to use a pin that does not support this mode of operation' + str(e)})  # TODO localize
        except Exception:
            return Response({'error': str(sys.exc_info())})

        return Response({})


class StopProgramView(APIView, LoginRequiredMixin):
    def post(self, request):
        # TODO proper input validation
        program = Program.objects.get(pk=int(request.data['pk']))

        program.running = False

        program.save()

        # TODO proper response
        return Response({})


class EditProgramView(APIView, LoginRequiredMixin):
    def post(self, request):
        # TODO proper input validation
        if request.data['pk'] != '':
            program = Program.objects.get(pk=int(request.data['pk']))

            program.code = str(request.data['code'])
            program.blockly_string = str(request.data['blockly_string'])

            program.save()
        # TODO proper response
        return Response({})
