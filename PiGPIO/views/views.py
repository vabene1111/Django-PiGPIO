from django.shortcuts import render
from django_tables2 import RequestConfig

from PiGPIO.models import ProgramStep, Program
from PiGPIO.tables import ProgramStepTable


def index(request):
    table = ProgramStepTable(ProgramStep.objects.all())
    RequestConfig(request, paginate={'per_page': 25}).configure(table)

    return render(request, 'index.html', {"test": table})


def program(request, pk):
    # program_steps = ProgramStepTable(ProgramStep.objects.filter(program_id=pk).all())
    # RequestConfig(request, paginate={'per_page': 25}).configure(program_steps)
    program_steps = ProgramStep.objects.filter(program_id=pk).all()

    program_info = Program.objects.get(pk=pk)

    return render(request, 'program.html', {'program_info': program_info, 'program_steps': program_steps})
