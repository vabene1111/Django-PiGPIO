import django_tables2 as tables
from django.utils.html import format_html
from django.utils.translation import gettext as _
from django_tables2.utils import A  # alias for Accessor

from .models import *


class ProgramTable(tables.Table):
    id = tables.LinkColumn('edit_program', args=[A('id')])

    class Meta:
        model = Program
        fields = ('id', 'name', 'description')


class ProgramStepTable(tables.Table):

    class Meta:
        model = ProgramStep
        orderable = False
        fields = ('id', 'type', 'data')
