from django.shortcuts import render
from django_tables2 import RequestConfig

from PiGPIO.models import ProgramStep
from PiGPIO.tables import ProgramStepTable


def index(request):
    table = ProgramStepTable(ProgramStep.objects.all())
    RequestConfig(request, paginate={'per_page': 25}).configure(table)

    return render(request, 'index.html', {"test": table})


def program(request):
    table = ProgramStepTable(ProgramStep.objects.all())
    RequestConfig(request, paginate={'per_page': 25}).configure(table)

    return render(request, 'program.html', {"program_steps": table})
