from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from PiGPIO.models import Program, Dashboard


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

    return render(request, 'remote.html', {'pins': pins})


def test(request):
    return render(request, 'test.html', {})
