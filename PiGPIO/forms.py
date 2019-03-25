from django import forms
from django.forms import widgets
from django.utils.translation import gettext as _

from PiGPIO.models import Program


class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = ('name', 'description','logging')
