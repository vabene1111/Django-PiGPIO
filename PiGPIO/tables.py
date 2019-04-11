import django_tables2 as tables
from django_tables2.utils import A  # alias for Accessor

from django.utils.translation import gettext as _

from .models import *


class ProgramTable(tables.Table):
    id = tables.LinkColumn('edit_program', args=[A('id')])
    code = tables.TemplateColumn(
        "<a href='{% url 'program' record.id %}' class='btn btn-success'><i class='fas fa-code'></i></a>")

    class Meta:
        model = Program
        fields = ('id', 'name', 'description', 'code')


class DashboardTable(tables.Table):
    id = tables.LinkColumn('edit_dashboard', args=[A('id')])

    class Meta:
        model = Dashboard
        fields = ('id', 'name', 'text', 'row', 'col')
