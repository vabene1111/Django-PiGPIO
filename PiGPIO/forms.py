from django import forms
from django.utils.translation import gettext as _

from PiGPIO.models import Program


class ProgramForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea)
    code = forms.CharField(disabled=True, widget=forms.Textarea)
    blockly_string = forms.CharField(disabled=True, widget=forms.Textarea)

    class Meta:
        model = Program
        fields = ('name', 'description', 'code', 'blockly_string')
