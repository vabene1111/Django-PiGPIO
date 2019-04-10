from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from PiGPIO.models import Program, Dashboard


@login_required
def index(request):
    buttons = Dashboard.objects.all()

    return render(request, 'index.html', {'buttons': buttons})


@login_required
def blockly(request, pk):
    return render(request, 'program_blockly.html', {'program': Program.objects.get(pk=pk)})


def test(request):
    return render(request, 'test.html', {})
