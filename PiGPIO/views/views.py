from django.shortcuts import render
from django_tables2 import RequestConfig

from PiGPIO.models import ProgramStep, Program
from PiGPIO.tables import ProgramStepTable

from PiGPIO.interpreter import *


def index(request):
    table = ProgramStepTable(ProgramStep.objects.all())
    RequestConfig(request, paginate={'per_page': 25}).configure(table)

    return render(request, 'index.html', {"test": table})


def program(request, pk):
    # program_steps = ProgramStepTable(ProgramStep.objects.filter(program_id=pk).all())
    # RequestConfig(request, paginate={'per_page': 25}).configure(program_steps)
    program_steps = ProgramStep.objects.filter(program_id=pk).all().order_by('num')

    program_info = Program.objects.get(pk=pk)

    return render(request, 'program.html', {'program_info': program_info, 'program_steps': program_steps})


def blocky(request):
    return render(request, 'blocky.html')


def test(request):
    tokens = lex('if x==1 then dont_use_this = True else dont_use_this = False end')
    result = parse(tokens)

    if not result:
        print('Praser failed')

    ast = result.value
    env = {}
    ast.eval(env)

    return render(request, 'test.html', {'test': env})
