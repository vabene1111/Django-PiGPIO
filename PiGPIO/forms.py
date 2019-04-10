from django import forms
from django.utils.translation import gettext as _

from PiGPIO.models import Program, Dashboard


class ProgramForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea, required=False)
    code = forms.CharField(disabled=True, widget=forms.Textarea, required=False)
    blockly_string = forms.CharField(disabled=True, widget=forms.Textarea, required=False)

    class Meta:
        model = Program
        fields = ('name', 'description', 'code', 'blockly_string')


class DashboardForm(forms.ModelForm):
    def validate(self, value):
        """Check if value consists only of valid emails."""
        # Use the parent's handling of required fields, etc.
        super().validate(value)

    class Meta:
        model = Dashboard
        fields = ('name', 'text', 'row', 'col', 'background_color', 'font_color', 'icon', 'program')
