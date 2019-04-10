from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from django_tables2 import RequestConfig
from django.utils.translation import gettext as _

from PiGPIO.models import Program, Dashboard
from PiGPIO.tables import ProgramTable, DashboardTable


@login_required
def program(request):
    table = ProgramTable(Program.objects.all())
    RequestConfig(request, paginate={'per_page': 25}).configure(table)

    return render(request, 'generic/list_template.html', {'title': _("Program"), 'table': table})


@login_required
def dashboard(request):
    table = DashboardTable(Dashboard.objects.all())
    RequestConfig(request, paginate={'per_page': 25}).configure(table)

    return render(request, 'generic/list_template.html', {'title': _("Dashboard Buttons"), 'table': table})
