from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from PiGPIO.models import Program, Dashboard
from PiGPIO.helper import raspi


@login_required
def index(request):
    buttons = Dashboard.objects.all()

    return render(request, 'index.html', {'buttons': buttons})


@login_required
def program(request, pk):
    return render(request, 'program_blockly.html', {'program': Program.objects.get(pk=pk)})


@login_required
def remote(request):
    pins = []

    for i in range(1, 41, 2):
        r1 = str(i)
        if i < 10:
            r1 = '0' + str(i)

        r2 = str(i + 1)
        if (i + 1) < 10:
            r2 = '0' + str(i + 1)

        pins.append({'r': r1, 'l': r2})

    raspi.set_mode(0)
    for x in pins:
        try:
            raspi.setup_pin(int(x['r']), 1)
            raspi.set_output(int(x['r']), 0)
        except:
            x['error_r'] = 'error'
            pass

        try:
            raspi.setup_pin(int(x['l']), 1)
            raspi.set_output(int(x['l']), 0)
        except:
            x['error_l'] = 'error'
            pass

    return render(request, 'remote.html', {'pins': pins})


def test(request):
    return render(request, 'test.html', {})
