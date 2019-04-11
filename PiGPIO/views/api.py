import sys
from threading import Thread

from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.response import Response
from rest_framework.views import APIView

from PiGPIO.helper import raspi, UndefinedPinException, OutputNotSupportedException, ListNotSupportedException
from PiGPIO.models import Program, Log
from django.utils.translation import gettext as _

from PiGPIO.serializers import SetPinSerializer


class SetPinView(APIView, LoginRequiredMixin):
    serializer_class = SetPinSerializer

    def post(self, request):
        raspi.set_mode(0)

        results = SetPinSerializer(request.data, many=False).data

        raspi.setup_pin(results['pin'], results['mode'])
        raspi.set_output(results['pin'], results['state'])
        return Response({})


class RunProgramView(APIView, LoginRequiredMixin):
    def post(self, request):
        run_program(request.data['pk'])

        return Response({})


def start_new_thread(function):
    def decorator(*args, **kwargs):
        t = Thread(target=function, args=args, kwargs=kwargs)
        t.daemon = True
        t.start()

    return decorator


@start_new_thread
def run_program(program_id):
    program = Program.objects.get(pk=program_id)
    program.running = True
    program.save()

    Log.objects.all().delete()

    raspi.set_mode(0)

    try:
        exec(program.code)
        raspi.log(_('INFO: Program finished successfully!'))
    except UndefinedPinException:
        raspi.log('ERROR: Trying to set status of undefined pin')  # TODO localize
    except OutputNotSupportedException as e:
        raspi.log('ERROR: There was an error trying to output on pin' + str(e))  # TODO localize
    except ListNotSupportedException as e:
        raspi.log('ERROR: Trying to pass list ' + str(e) + ' to function not supporting lists.')  # TODO localize
    except Exception:
        raspi.log(str(sys.exc_info()))

    program.running = False
    program.save()
    raspi.log('__DONE__')


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

        done = False
        log_string = ""
        for log in logs:
            if log.data == "__DONE__":
                done = True
            else:
                log_string = log_string + log.created_at.strftime("%H:%M:%S:%f") + ' ' + log.data + '\n'
            Log.objects.get(pk=log.pk).delete()

        return Response({'log': log_string, 'program_finished': done})
