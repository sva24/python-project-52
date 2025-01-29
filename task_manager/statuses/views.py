from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from task_manager.mixins import (DeleteProtectedObjectMixin, LoginCheckMixin,
                                 TemplateContextMixin)

from .models import Status

# Create your views here.


class StatusListView(LoginCheckMixin, ListView):
    model = Status
    template_name = "show_statuses.html"
    context_object_name = "statuses"


class StatusCreateView(LoginCheckMixin, SuccessMessageMixin, CreateView):
    model = Status
    fields = ["name"]
    template_name = "create.html"
    success_url = reverse_lazy("statuses")
    success_message = _("Status created successfully")


class StatusUpdateView(LoginCheckMixin, SuccessMessageMixin, UpdateView):
    model = Status
    fields = ["name"]
    template_name = "./update.html"
    success_url = reverse_lazy("statuses")
    success_message = _("Status updated successfully")


class StatusDeleteView(
    LoginCheckMixin,
    TemplateContextMixin,
    SuccessMessageMixin,
    DeleteProtectedObjectMixin,
    DeleteView,
):
    model = Status
    template_name = "confirm_delete.html"
    success_url = reverse_lazy("statuses")
    page_title = _("Update status")
    submit_button_text = _("Yes, delete")
    success_message = _("Status successfully deleted")
    protected_error_message = _("Cannot delete status because it is in use")
    protect_redirect = "statuses"
