from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import CreateView

from PiGPIO.forms import ProgramForm
from PiGPIO.models import Program


class ProgramCreate(LoginRequiredMixin, CreateView):
    template_name = "generic/new_template.html"
    model = Program
    form_class = ProgramForm
    success_url = reverse_lazy('list_program')

    def get_context_data(self, **kwargs):
        context = super(ProgramCreate, self).get_context_data(**kwargs)
        context['title'] = _("Program")
        return context


