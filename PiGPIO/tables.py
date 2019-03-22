import django_tables2 as tables
from django.utils.html import format_html
from django.utils.translation import gettext as _
from django_tables2.utils import A  # alias for Accessor

from .models import *


class ProgramTable(tables.Table):
    id = tables.LinkColumn('edit_program', args=[A('id')])
    code = tables.TemplateColumn(
        "<a href='{% url 'program' record.id %}' class='btn btn-success'><i class='fas fa-code'></i></a>")

    class Meta:
        model = Program
        fields = ('id', 'name', 'description', 'code')


class ProgramStepTable(tables.Table):

    class Meta:
        model = ProgramStep
        orderable = False
        fields = ('num', 'pin', 'type', 'data', 'successor_true', 'successor_false')
