from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import CreateView

from PiGPIO.forms import ProgramForm, DashboardForm
from PiGPIO.models import Program, Dashboard


class ProgramCreate(LoginRequiredMixin, CreateView):
    template_name = "generic/new_template.html"
    model = Program
    form_class = ProgramForm
    success_url = reverse_lazy('list_program')

    def get_context_data(self, **kwargs):
        context = super(ProgramCreate, self).get_context_data(**kwargs)
        context['title'] = _("New Program")
        return context


class DashboardCreate(LoginRequiredMixin, CreateView):
    template_name = "generic/new_template.html"
    model = Dashboard
    form_class = DashboardForm
    success_url = reverse_lazy('list_dashboard')

    def get_context_data(self, **kwargs):
        context = super(DashboardCreate, self).get_context_data(**kwargs)
        context['title'] = _("New Dashboard Button")
        return context
