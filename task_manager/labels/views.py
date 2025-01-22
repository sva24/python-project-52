from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Label
from task_manager.mixins import TemplateContextMixin, LoginCheckMixin
from django.utils.translation import gettext_lazy as _


class LabelListView(LoginCheckMixin, ListView):
    model = Label
    template_name = 'show_labels.html'
    context_object_name = 'labels'
    success_url = reverse_lazy('labels')
    page_title = _("Create label")
    submit_button_text = _("Create")


class LabelCreateView(LoginCheckMixin, CreateView):
    model = Label
    fields = ['name']
    template_name = 'create_label.html'
    success_url = reverse_lazy('labels')
    success_message = _("The label was successfully created.")


class LabelUpdateView(LoginCheckMixin,
                      TemplateContextMixin,
                      UpdateView):
    model = Label
    fields = ['name']
    template_name = 'create_label.html'
    success_url = reverse_lazy('labels')
    page_title = _("Change label")
    submit_button_text = _("Update")
    success_message = _("The label has been changed successfully.")


class LabelDeleteView(LoginCheckMixin,
                      TemplateContextMixin,
                      DeleteView):
    model = Label
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('labels')
    page_title = _("Delete label")
    button_text = _("Delete")
    success_message = _("The label has been successfully removed")

