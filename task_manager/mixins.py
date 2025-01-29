from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import ProtectedError
from django.shortcuts import get_object_or_404, redirect
from django.utils.translation import gettext_lazy as _

from .tasks.models import Task
from .users.models import CustomUser


class LoginCheckMixin(LoginRequiredMixin):
    def get_login_message(self):
        return _("You are not logged in! Please sign in.")

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, self.get_login_message())
            return redirect("login")
        return super().dispatch(request, *args, **kwargs)


class PermissionCheckMixin:
    def get_permission_message(self):
        return _("You do not have permission to change another user.")

    def dispatch(self, request, *args, **kwargs):
        user_to_edit = get_object_or_404(CustomUser, pk=kwargs.get("pk"))

        if request.user != user_to_edit:
            messages.error(request, self.get_permission_message())
            return redirect("users")

        return super().dispatch(request, *args, **kwargs)


class TemplateContextMixin:
    page_title = ""
    submit_button_text = ""

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = self.page_title
        context["submit_button_text"] = self.submit_button_text
        return context


class TaskOwnerCheckMixin:
    owner_field = None

    def get_permission_message(self):
        return _("A task can only be deleted by its author")

    def dispatch(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get("pk"))
        owner = getattr(task, self.owner_field)

        if owner != request.user:
            messages.error(request, self.get_permission_message())
            return redirect("tasks")

        return super().dispatch(request, *args, **kwargs)


class DeleteProtectedObjectMixin:
    protected_error_message = ""
    protect_redirect = ""

    def post(self, request, *args, **kwargs):
        obj = self.get_object()
        try:
            obj.delete()
            messages.success(request, self.success_message)
            return redirect(self.protect_redirect)
        except ProtectedError:
            messages.error(request, self.protected_error_message)
            return redirect(self.protect_redirect)


class PreventLabelDeletionMixin:
    deletion_protected_message = ""
    protect_redirect_url = ""

    def post(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.task_set.exists():
            messages.error(request, self.deletion_protected_message)
            return redirect(self.protect_redirect_url)

        return super().post(request, *args, **kwargs)
