from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from task_manager.mixins import LoginCheckMixin, TemplateContextMixin
from .models import Status
from django.utils.translation import gettext_lazy as _

# Create your views here.


class StatusListView(LoginCheckMixin, ListView):
    model = Status
    template_name = 'show_statuses.html'
    context_object_name = 'statuses'


class StatusCreateView(LoginCheckMixin, CreateView):
    model = Status
    fields = ['name']
    template_name = 'create.html'
    success_url = reverse_lazy('statuses')

    def form_valid(self, form):
        messages.success(self.request, "Status created successfully.")
        return super().form_valid(form)


class StatusUpdateView(LoginCheckMixin, UpdateView):
    model = Status
    fields = ['name']
    template_name = './update.html'
    success_url = reverse_lazy('statuses')

    def form_valid(self, form):
        messages.success(self.request, "Status updated successfully.")
        return super().form_valid(form)


class StatusDeleteView(LoginCheckMixin,
                       TemplateContextMixin,
                       DeleteView):
    model = Status
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('statuses')
    page_title = _("Update status")
    submit_button_text = _("Yes, delete")
