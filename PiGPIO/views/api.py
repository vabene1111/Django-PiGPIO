import sys

from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.response import Response
from rest_framework.views import APIView

from PiGPIO.helper import raspi, UndefinedPinException, OutputNotSupportedException, ListNotSupportedException
from PiGPIO.models import Program, Log
from django.utils.translation import gettext as _


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
            raspi.log(_('INFO: Program finished successfully!'))
        except UndefinedPinException:
            raspi.log('ERROR: Trying to set status of undefined pin')  # TODO localize
        except OutputNotSupportedException as e:
            raspi.log('ERROR: Outputting on pin ' + str(e) + ' is not supported by this model.')  # TODO localize
        except ListNotSupportedException as e:
            raspi.log('ERROR: Trying to pass list ' + str(e) + ' to function not supporting lists.')  # TODO localize
        except Exception:
            raspi.log(str(sys.exc_info()))

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


class PopLogView(APIView, LoginRequiredMixin):
    def post(self, request):
        logs = Log.objects.all()

        log_string = ""
        for log in logs:
            log_string = log_string + log.created_at.strftime("%H:%M:%S:%f") + ' ' + log.data + '\n'
            Log.objects.get(pk=log.pk).delete()

        return Response({'log': log_string})
