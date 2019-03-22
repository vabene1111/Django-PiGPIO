from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.utils.translation import gettext as _
from django.views.generic import UpdateView, DeleteView

from PiGPIO.forms import ProgramForm
from PiGPIO.models import Program


class ProgramUpdate(LoginRequiredMixin, UpdateView):
    model = Program
    form_class = ProgramForm
    template_name = "generic/edit_template.html"

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, _('Changes saved!'))
        return super(ProgramUpdate, self).form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, _('Error saving changes!'))
        return super(ProgramUpdate, self).form_valid(form)

    def get_success_url(self):
        return reverse('edit_program', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super(ProgramUpdate, self).get_context_data(**kwargs)
        context['title'] = _("Program")
        return context


# Generic Delete views

def delete_redirect(request, name, pk):
    return redirect(('delete_' + name), pk)


class ProgramDelete(LoginRequiredMixin, DeleteView):
    template_name = "generic/delete_template.html"
    model = Program
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(ProgramDelete, self).get_context_data(**kwargs)
        context['title'] = _("Program")
        return context

