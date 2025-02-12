from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from task_manager.mixins import (
    LoginCheckMixin,
    PreventLabelDeletionMixin,
    TemplateContextMixin,
)

from .models import Label


class LabelListView(LoginCheckMixin, ListView):
    model = Label
    template_name = "show_labels.html"
    context_object_name = "labels"
    success_url = reverse_lazy("labels")
    page_title = _("Create label")
    submit_button_text = _("Create")


class LabelCreateView(
    LoginCheckMixin, SuccessMessageMixin, TemplateContextMixin, CreateView
):
    model = Label
    fields = ["name"]
    template_name = "create_label.html"
    success_url = reverse_lazy("labels")
    success_message = _("The label was successfully created.")
    page_title = _("Create label")
    submit_button_text = _("Create")


class LabelUpdateView(
    LoginCheckMixin, SuccessMessageMixin, TemplateContextMixin, UpdateView
):
    model = Label
    fields = ["name"]
    template_name = "create_label.html"
    success_url = reverse_lazy("labels")
    page_title = _("Change label")
    submit_button_text = _("Update")
    success_message = _("The label has been changed successfully.")


class LabelDeleteView(
    LoginCheckMixin,
    TemplateContextMixin,
    PreventLabelDeletionMixin,
    SuccessMessageMixin,
    DeleteView,
):
    model = Label
    template_name = "confirm_delete.html"
    success_url = reverse_lazy("labels")
    page_title = _("Delete label")
    button_text = _("Delete")
    success_message = _("The label has been successfully removed")
    deletion_protected_message = _(
        "The label cannot be deleted because it is in use."
    )
    protect_redirect_url = "labels"
