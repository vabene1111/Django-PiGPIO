from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django_tables2 import RequestConfig

from PiGPIO.models import ProgramStep, Program
from PiGPIO.tables import ProgramStepTable


@login_required
def index(request):
    table = ProgramStepTable(ProgramStep.objects.all())
    RequestConfig(request, paginate={'per_page': 25}).configure(table)

    return render(request, 'index.html', {"test": table})


@login_required
def blockly(request, pk):

    return render(request, 'program_blockly.html', {'program': Program.objects.get(pk=pk)})


def test(request):
    return render(request, 'test.html', {})
